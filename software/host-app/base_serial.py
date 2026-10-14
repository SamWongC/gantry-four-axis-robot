# scara  ....
import math
from re import U
import time
from struct import unpack,pack
import serial
import serial.tools.list_ports
import logging
#
# 串口程序使用线程
# 发送指令，在指定时间等待应答：返回结果为应答数据或者指令超时
# 如是广播指令则无需等待应答
# 使用线程时，发送后如何等待应答，在指令必须发送到位时
# 对于连续读状态值，可以在线程内使用定时器连续发送读状态指令，返回数据通过事件发送给主线程
#

# 串口通信指令  
# 串口命令帧格式: AA AA LEN ADR FN SN DATA CS FF
#    
'''
    usage:
        a = Base_Serial(Dev_TYPE)
        a.open_port('port_name')
        a.read_dev_adr()  
'''

# 私有协议串口通信基础类
class Base_Serial(object):

    FRAME_LEN_MIN = 8  # 最小帧长度，无数据域 AA AA LEN ADR FN SN CS FF
    BOF1 = 0xAA        # 帧头标志字节1
    BOF2 = 0xAA        # 帧头标志字节2
    EOF  = 0xFF        # 帧尾标志字节
                       # 使用 MySerial.EOF访问类的变量
    
    # 创建类实例时，指定设备地址和设备类型
    def __init__(self,adr=254, fn=0xD1):
        self.errMsg = ''          # 错误信息   
        self.fn = fn              # 设备类型
        self.adr = adr            # 设备地址     
        self.ports = []           # 系统串口列表
        self.serPort = None       # 设备直连串口
        self.rx_time = 1.0        # 串口接收超时时间，单位秒
        self.txBuf = bytearray()  # 发送缓冲区
        self.rxBuf = bytearray()  # 接收缓冲区

        self.frame_head = bytearray.fromhex('AAAA') # 帧头标识符
        self.frame_end = 0xFF     # 帧尾
        self.rxLen = 0            # 接收帧长度

    # 获取系统可用的串口，返回可用串口名称列表
    def get_ports(self):
        self.port_list = list(serial.tools.list_ports.comports())
        self.ports.clear()
        if len(self.port_list):
            for each in self.port_list:
                self.ports.append(each[0])
        
        return self.ports   # 返回可用的串口列表
    
    # 关闭串口
    def close_port(self):
        if self.serPort:
            self.serPort.close()  
            self.serPort = None  

    # 打开串口，缺省波特率115200
    def open_port(self, port=None, baudrate=115200):
        # 不指定port时，用于软件模拟串口返回数据测试
        if port is None: 
            self.serPort = True
            return True
        # 打开指定的port端口
        try:
            self.serPort = serial.Serial(port, baudrate, timeout=1, write_timeout=1) # 读写超时均为1s
            return True
        except Exception as e:
            self.errMsg = repr(e)    # 保存异常信息
            self.serPort = None      # 没有可用串口
            return False
    
    # 串口发送数据，数据发送前清除发送和接收缓冲区
    def send_raw(self, txBuf):
        if self.serPort and self.serPort.isOpen():
            self.serPort.reset_input_buffer()
            self.serPort.reset_output_buffer()
            self.serPort.write(txBuf)
    
    # 计算累加校验和,输入参数bytearray
    def crc_calc(self, buf):
        cs = 0
        for each in buf: cs += each
        return cs & 0xFF
    
    # 校验和检查,如果接收帧中的cs==0，则屏蔽cs校验以方便手动输入调试命令        
    def check_crc(self,buf):
        cnt = len(buf)
        cs = buf[cnt-2]
        cs1 = self.crc_calc(buf[:cnt-2])
        if cs == cs1 or 0 == cs:   # CS=0屏蔽校验
            return True
        else:
            return False
    
    # 生成命令帧 ： Adr, Fn由类变量指定，Sn和数据与由参数输入
    # 数据域为包含data的bytearray
    # AA AA Len Adr Fn Sn Data[0:Len] CS FF的格式
    def make_cmd(self, sn, dbuf):
        self.txBuf.clear()
        self.txBuf.append(Base_Serial.BOF1)        # 帧起始符1
        self.txBuf.append(Base_Serial.BOF2)

        self.txBuf.append(len(dbuf))               # 参数长度
        self.txBuf.append(self.adr)
        self.txBuf.append(self.fn)
        self.txBuf.append(sn) 
        self.txBuf += dbuf                         # 数据参数
        
        cs = self.crc_calc(self.txBuf)
        self.txBuf.append(cs)                      # CRC
        self.txBuf.append(Base_Serial.EOF)         # 帧结束符       
        #for i in range(len(self.txBuf)):
        #    print(self.txBuf[i])
        return self.txBuf
        
    # 向串口发送命令
    def send_cmd(self, sn, dbuf=bytearray()):
        self.make_cmd(sn, dbuf)
        self.send_raw(self.txBuf)                   # send to uart port
        #print(txBuf)

    # 调试函数，返回16进制的发送命令    
    def get_txBuf_hexStr(self):
        return ' '.join(format(x, '02X') for x in self.txBuf)

    def get_rxBuf_hexStr(self):
        return ' '.join(format(x, '02X') for x in self.rxBuf)
    
    #def hexStr(self, buf):
    #    return ' '.join(format(x, '02X') for x in buf)

    # 从串口接收数据，如果规定时间内没收到数据则中止接收
    # rxBuf为接收到的数据帧
    # 返回数据为接收帧的数据域
    def recv_data(self):
        self.rxBuf.clear()         # 清除接收缓冲区
        if self.serPort is None or not self.serPort.isOpen():
            return  self.rxBuf     # 如果串口不可用则返回
        
        ts = time.time()
        self.rxBuf.clear()
        rxData = bytearray()
        while time.time()-ts < self.rx_time:           # 读串口1s不回数则结束
            rx_len = self.serPort.in_waiting
            if rx_len:
                rxData += self.serPort.read(rx_len)    # 串口接收数据
                fh_n = rxData.find(self.frame_head)    # 寻找帧头
                if len(rxData)<fh_n+3: continue        # AA AA LEN,继续接收
            
                f_len = rxData[fh_n+2]+8
                if len(rxData) < fh_n+f_len: continue  # 继续接收
                
                if rxData[fh_n+f_len-1] == self.frame_end:       # 找到帧尾
                    if self.check_crc(rxData[fh_n:fh_n+f_len]):  # 数据校验正确
                        self.rxBuf = rxData[fh_n:fh_n+f_len]     # 提取接收数据
                        return self.rxBuf[6:-2]  
        
        # print(self.rxBuf)                                        # 串口数据接收结束
        return self.rxBuf
        
    # 检查指令是否接收到指令接收成功应答数据：0x01 0x01
    def check_cmd_ack(self):
        rv = False
        if len(self.rxBuf): # 接收到数据
            dbuf = self.rxBuf[6:-2]
            if dbuf[0]==0x01 and dbuf[1]==0x01:
                rv = True
        return rv

    # 返回数据的指令,输入参数Sn,返回数据域：bytearray()
   
    # 读数据指令，返回数据域：bytearray()
    # 如果tf_buf是AA AA ... FF格式的指令，则直接解析返回数据域
    # tf_buf可以用于软件模拟串口返回数据
    # 如果tf_buf内容不是合法帧数据，则发送命令读串口返回数据
    # self.txBuf保存串口返回的原始数据
    def read_cmd_data(self, sn, dbuf=bytearray(), tf_buf=bytearray()):
        if 8 <= len(tf_buf):
            if 0xAA == tf_buf[0] and 0xAA == tf_buf[1]:
                self.rxBuf = tf_buf
                rbuf = tf_buf[6:-2]                # rbuf为接收到的数据域
            else:
                rbuf = bytearray()    
                self.rxBuf = rbuf                  # 不正确的帧
        else:
            self.send_cmd(sn, dbuf)                # 发送命令
            rbuf = self.recv_data()                # 接收数据
            if 0 == len(rbuf): rbuf = bytearray()  # 未接收到数据
        #print(self.txBuf)
        return rbuf 

    # 模拟串口返回数据,dbuf为bytearray
    def make_recv_data(self,sn,dbuf):
        recvDat = bytearray()
        recvDat.append(Base_Serial.BOF1)    # 帧起始符1
        recvDat.append(Base_Serial.BOF2)
        recvDat.append(len(dbuf))           # 参数长度
        recvDat.append(self.adr)
        recvDat.append(self.fn)
        recvDat.append(sn) 
        recvDat += dbuf                     # 数据参数
        
        cs = self.crc_calc(recvDat)
        recvDat.append(cs)                  # CRC
        recvDat.append(Base_Serial.EOF)     # 帧结束符        
        return recvDat

    # 读设备信息: 地址，设备类型(fn)，软件版本
    def read_dev_msg(self, tbuf=bytearray()):
        return self.read_cmd_data(0x01, tf_buf=tbuf)
 
    # 读设备地址,获取设备地址和设备类型
    # 读取成功，则设置类的adr和fn变量    
    # 读取不成功 adr == 255
    def read_dev_adr(self, tbuf=bytearray()):
        self.adr = 255
        rv = self.read_cmd_data(0xF1, tf_buf=tbuf)
        if len(rv) > 0:
            self.adr = rv[0]
        else:
            self.adr = 255
        return self.adr
    
    # 写设备地址
    def write_dev_adr(self, dev_adr, tbuf=bytearray()):
        self.adr = 255
        dbuf = bytearray()
        dbuf.append(dev_adr)
        self.read_cmd_data(0xFA, dbuf,tf_buf=tbuf)
        return self.check_cmd_ack()
