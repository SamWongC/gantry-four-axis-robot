import time
import queue
from struct import unpack, pack
import logging
from base_serial import Base_Serial

# 与SCARA控制器通信的串口类
class SCARA_Serial(Base_Serial):
    def __init__(self, adr=254, fn=0xD1):
        super().__init__(adr, fn)

        log_level = logging.DEBUG                # 信息输出级别
        log_level = logging.WARNING              # 信息输出级别
        logging.basicConfig(level=log_level)
        self.log = logging.getLogger()
        self.log.setLevel(level=log_level)        

        self.cmd_queue = queue.Queue()           # FIFO指令缓冲区
        self.CMD_BUF_LEN = 200                   # 控制器命令缓冲区长度
        self.cnt = 0

    # 电机控制命令添加到队列中
    # 命令添加没有限制，队列容量只受限于计算机内容容量
    # 添加到队列中的命令有两种：正常的电机控制命令，arr>65535的命令
    # arr>65535的命令为启动命令，在发送的时候会替换为启动指令
    def cmd_queue_put(self, cmd):
        self.cmd_queue.put(cmd)

    # 发送指令到控制器，发送成功返回1，发送失败返回0
    def cmd_queue_send(self):
        if self.cmd_queue.qsize() > 0:
            cmd = self.cmd_queue.get()
            a1, p1, e1, a2, p2, e2, a3, p3, e3, a4, p4, e4 = cmd
            # 检查是否是 启动控制器缓冲区命令运行 指令
            if a1 > 65535 and a2 > 65535 and a3 > 65535 and a4 > 65535:
                
                # 发送启动指令前先确认控制器是否停止运行，启动时会提取一条缓冲区中的命令
                # 不能重复发送启动命令
                
                rv = self.cmd_run_start()
                print('识别并发送上位机队列中启动指令')
            else:
                rv = self.cmd_send(cmd)
            return rv

    # 同步队列指令到控制器 - 发送一组指令
    def cmd_queue_sync(self):
        while self.cmd_queue.qsize() > 0:
            cmd_len = self.cmd_buf_len()            # 获取控制器可写入指令数量
            if cmd_len < 2:                        # 设为控制器缓冲区长度的1/4
                if self.cmd_run_status() == 0:      # 如果缓冲区指令没运行，则启动
                    self.cnt += 1                   # 控制器的可写入命令长度为0时计数
                    if self.cnt > 10:               # 自动插入启动控制器缓冲区命令运行指令
                        self.cmd_run_start()
                        print('自动发送 控制器缓冲区命令运行 指令')
                else:
                    self.cnt = 0
                continue
            
            if self.cmd_queue.qsize() < cmd_len:    # 检查指令队列长度
                cmd_len = self.cmd_queue.qsize()
            #
            print(f'发送了  {cmd_len} / {self.cmd_queue.qsize()}  条指令 --->')
            n = 0
            while n < cmd_len:
                if self.cmd_queue_send(): n = n + 1

    # 发送电机控制指令: 0x21 ，指令存入控制器的指令缓冲区
    # wp=( arr1, pcnt1, pen1, arr2, pcnt2, pen2, arr3, pcnt3, pen3, arr4, pcnt4, pen4 )
    def cmd_send(self, wp, tbuf=bytearray()):
        a1, p1, e1, a2, p2, e2, a3, p3, e3, a4, p4, e4 = wp
        dbuf = pack('<HhBHhBHhBHhB', a1, p1, e1, a2, p2, e2, a3, p3, e3, a4, p4, e4)
        # 发送3次，有1次成功则返回True
        self.fn += 1  # 在scara控制器的通信帧中，fn充当帧序列号使用
        if self.fn > 255 : self.fn = 0
        #print(f'帧序列号-{self.fn}')
        for n in range(3):
            self.read_cmd_data(0x21, dbuf, tf_buf=tbuf)
            if self.check_cmd_ack(): return True
        # 发送失败
        return False

    # 发送停止电机控制指令，指令存入控制器的指令缓冲区
    def cmd_run_stop(self, tbuf=bytearray()):
        wp = (0,1,0, 0,1,0, 0,1,0, 0,1,0,)
        return self.cmd_send(wp)

    # 启动缓冲区中命令运行
    def cmd_run_start(self, tbuf=bytearray()):
        dbuf = bytearray()
        # 最多尝试发送3次，有1次成功则返回True
        for n in range(3):
            self.read_cmd_data(0x13, dbuf, tf_buf=tbuf)
            if self.check_cmd_ack(): return True
        # 发送失败
        return False

    # 获取控制器缓冲区命令运行状态
    # 返回1-正在运行， 返回0-停止运行    
    def cmd_run_status(self, tbuf=bytearray()):
        rv = False
        dbuf = bytearray()
        self.read_cmd_data(0x1B, dbuf, tf_buf=tbuf)   # 发送指令     
        if len(self.rxBuf):                           # 接收指令返回数据
            dbuf = self.rxBuf[6:-2]                   # 提取数据                      
            if dbuf[0] ==  dbuf[1] :                  # 
                if dbuf[0] == 1:
                    rv = True
        return rv    

    # 获取控制器命令缓冲区可用长度
    def cmd_buf_len(self, tbuf=bytearray()):
        buf_len = -1
        dbuf = bytearray()
        self.read_cmd_data(0x1A, dbuf, tf_buf=tbuf)   # 发送指令     
        if len(self.rxBuf):                           # 接收指令返回数据
            dbuf = self.rxBuf[6:-2]                   # 提取数据                      
            if dbuf[0] ==  dbuf[1] :                  # 
                buf_len  = dbuf[0]
        # 返回-1表示通信错误，返回0~200表示控制器可用命令缓冲区长度
        return buf_len
    #
    #  
    # 电机停止指令 : 0x11, 此指令立即执行
    def motor_stop(self, tbuf=bytearray()):
        dbuf = bytearray()
        self.read_cmd_data(0x11, dbuf, tf_buf=tbuf)
        return self.check_cmd_ack()

    # 电机位置置零, 控制器中会对电机运行脉冲计数
    # 电机回零时，清零位置计数器
    def postion_clear(self, tbuf=bytearray()):
        dbuf=bytearray()
        self.read_cmd_data(0x1C, dbuf,tf_buf=tbuf)
        return self.check_cmd_ack()

    # 读电机位置计数器
    def position_read(self, tbuf=bytearray()):
        rv = self.read_cmd_data(0x1F, tf_buf=tbuf)
        read_status = False
        if len(rv) == 16:
            pcnt1, pcnt2, pcnt3, pcnt4 = unpack('<IIII',rv)
            cnt = (pcnt1, pcnt2, pcnt3, pcnt4)
            read_status = True
        else:
            cnt = (-1, -1, -1, -1)

        return (read_status, cnt)
        
    # read limit switch status
    # return value: 1 - on; 0 - off; -1 - read error
    def read_limit_sw(self, tbuf=bytearray()):
        rv = self.read_cmd_data(0x1D, tf_buf=tbuf)
        #print('sw',rv)
        if len(rv)==2:
            sw, s1 = unpack('<BB',rv)
        else:
            sw = -1
        return sw    




    # 广播启动 ()
    def all_motor_run(self, rv, tbuf=bytearray()):
        dbuf = bytearray()
        a1, s1, p1, a2, s2, p2, a3, s3, p3, a4, s4, p4   = rv
        dbuf += pack('<IhBIhBIhBIhB', a1, s1, p1, a2, s2, p2, a3, s3, p3, a4, s4, p4)
        print('all motor run - ', a1, s1, p1, a2, s2, p2, a3, s3, p3, a4, s4, p4)
        adr = self.adr
        self.adr = 255
        self.read_cmd_data(0xFC, dbuf)
        #print(dbuf)
        self.adr = 1
        #time.sleep(0.5)
        if self.check_motor_ack():
            print('send cmd ok.')
            rv = True
        else:
            print('send cmd fail.')
            rv = False
        self.adr = adr
        return rv
    
    # 广播停机
    def all_motor_stop(self, tbuf=bytearray()):
        adr = self.adr
        self.adr = 255
        dbuf=bytearray()
        self.send_cmd(0xFE, dbuf)
    
    # ------------
    # 写电流脉冲参数,afs=(pulse_width, current_value, pulse_cnt)
    def write_pulse_para1(self, para, tbuf=bytearray()):
        vt, vi = para
        dbuf = pack('<HH', vt, vi)
        self.read_cmd_data(0x12, dbuf,tf_buf=tbuf)
        return self.check_cmd_ack()

    # ---------
    # motor_run, wp=(motor,direction,pulse count)
    def motor_run_old1(self, wp, tbuf=bytearray()):
        motor,dir,pulse = wp
        dbuf = pack('<BBI', motor,dir,pulse)
        self.read_cmd_data(0xAA, dbuf,tf_buf=tbuf)
        print(self.rxBuf)
        return self.check_cmd_ack()



# 测试代码
if __name__ == "__main__":
    a = SCARA_Serial(254, 0xD1)
    #a.log_off()
    comm_port = a.get_ports()
    print('available uart port:', comm_port)  # 获取系统可用串口

    if len(comm_port) > 0:
        a.open_port(comm_port[0])    # 打开第一个串口(系统只有一个串口）
        #adr = a.read_dev_adr()
        #print('device address = ', adr)
        #msg = a.read_dev_msg()
        #print('device message:', msg.decode())

        #print(a.position_read())
        #a.postion_clear()
        #print(a.position_read())
        #print(a.motor_stop())
        
        cmd_len = a.cmd_buf_len()
        print('控制器命令缓冲区可用长度=',cmd_len)


        # 指令发送过程
        # 轨迹规划产生的指令首先使用cmd_queue_put函数存放于上位机的命令队列中
        # 然后调用cmd_queue_sync同步函数将指令发送到下位机

        # 步距角1.0°，驱动器64细分，一圈 64*200脉冲
        arr = 300
        for n in range(64*2):
          a.cmd_queue_put((arr, -200, 1, arr, 200, 1, arr, 200, 1, arr, 200, 1))

        # 显示插入 启动下位机命令缓冲区开始运行 指令
        # 若不显式插入启动指令，上位机执行缓冲区同步时，若连续获取下位机的命令可用长度为0，则自动插入启动指令
        arr = 65535*10  # 启动指令
        a.cmd_queue_put((arr, 200, 1, arr, 200, 1, arr, 200, 1, arr, 200, 1))

        arr = 400
        for n in range(10*64):
          a.cmd_queue_put((arr, -200, 1, arr, 200, 1, arr, 200, 1, arr, 200, 1))

        
        print('\n同步队上位机列指令到控制器')
        a.cmd_queue_sync()

        # 延时等待控制器执行完缓冲区中命令
        n = 0
        while n < 10:
            print(f'控制器剩余命令{200 - a.cmd_buf_len()}')
            time.sleep(1)
            n += 1
            if a.cmd_buf_len() == 200:
                print('下位机命令缓冲区空')
                n = 11
        
        time.sleep(2)
        
        print('向控制器发送指令')

        arr = 500
        for n in range(10*64):
          a.cmd_queue_put((arr, -200, 1, arr, 200, 1, arr, 200, 1, arr, 200, 1))

        # 上位机同步指令时，只有在控制器可写指令长度为0时才会自动插入启动指令
        # 如果上位机发送的命令不足200条，需要插入启动控制器缓冲区命令运行指令
        # 同步函数会根据arr值识别出启动指令
        arr = 65535*10  # 启动指令
        a.cmd_queue_put((arr, 200, 1, arr, 200, 1, arr, 200, 1, arr, 200, 1))        
        
        print('\n同步上位机队列指令到控制器')
        a.cmd_queue_sync()
        print('队列剩余指令-', a.cmd_queue.qsize())

        #cmd_len = a.cmd_buf_len()
        #print('控制器命令缓冲区可用长度=',cmd_len)

 

        #print('--启动缓冲区命令运行')
        #print(a.cmd_run_start())

        a.close_port()

    #a.write_dev_adr(1)  # 配置控制器地址，一对一通信时写入