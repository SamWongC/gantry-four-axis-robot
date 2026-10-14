import sys
import time
import math
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem,QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QTimer

from scara_app import SCARA_APP
from scara_host_app_ui import Ui_Dialog
from App_lib import *

# PySide6 基础程序
class AppPyside6(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(AppPyside6, self).__init__()
        self.setupUi(self)
        self.file_path = None 
        # 如果是高分屏，屏幕有比例放大，则屏幕的宽和高需要按比例缩放
        # 获取屏幕宽和高
        #desktop = QGuiApplication.primaryScreen().availableGeometry()
        #self.dw = desktop.width()
        #self.dh = desktop.height()
        #self.window_center()

        self.msgbox = QMessageBox()
        self.msgbox.setStyleSheet("""
            QMessageBox {color: white; background-color: orange; font-size:12pt}
            """)

        # set app dialog title
        self.setWindowTitle('步进电机控制器测试程序')
        # set app dilog mode
        # self.setWindowFlags(Qt.FramelessWindowHint)
      
        # 打开串口
        self.pbUartOpen.clicked.connect(self.pbUartOpen_clicked)

        # 启动控制器缓冲区命令运行    发送运行指令
        self.pbCmdRun.clicked.connect(self.pbCmdRun_clicked)

        # 编码器计数清零
        self.encoder_clear.clicked.connect(self.encoder_clear_clicked)

        # 写电机驱动器的设备地址
        self.pbWriteDevAdr.clicked.connect(self.pbWriteDevAdr_clicked)

        # 添加顺时针1圈指令
        self.pbAppendCWCmd.clicked.connect(self.pbAppendCWCmd_clicked)
        # 添加逆时针1圈指令
        self.pbAppendCCWCmd.clicked.connect(self.pbAppendCCWCmd_clicked)

        # 队列指令同步到控制器 同步指令到缓冲区
        self.pbCmdQueueSync.clicked.connect(self.pbCmdQueueSync_clicked)
        
        # 添加电机停止命令到命令队列
        self.pbStop.clicked.connect(self.pbStop_clicked)
        # 添加命令到命令队列
        self.pbAppendCmd.clicked.connect(self.pbAppendCmd_clicked)
        # 发送命令到电机控制器
        self.pbCmdSend.clicked.connect(self.pbCmdSend_clicked)

        # 系统退出按钮
        self.pbExit.clicked.connect(self.pbExit_clicked)
        # 显示系统日期时间
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timer_out_func)
        self.timer.start()

        self.serial = SCARA_APP(254, 0xD1)  # 串口实例
        Update_Serial(self.serial, self.cbUartPort)
        Load_Uart_Cfg(self.cbUartPort)
        

    # 窗口居中显示
    def window_center(self):
        window = self.window()
        window.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                window.size(),
                QtGui.QGuiApplication.primaryScreen().availableGeometry(),
            )
        )
        # self.showNormal()

        self.resize(int(self.dw*1/2), int(self.dw*1/2*0.618))   
        self.setFixedSize(int(self.dw*1/2), int(self.dw*1/2*0.618))

    # 显示messagebox对话框
    def msgbox_show(self, title="错误", info="", btn=QMessageBox.Yes):
        self.msgbox.setWindowTitle(title)
        self.msgbox.setText(info)
        self.msgbox.setStandardButtons(btn)

        ret = self.msgbox.exec()
        if QMessageBox.Yes == ret: return True
        else: return False
    
    # 添加顺时针1圈指令
    def pbAppendCWCmd_clicked(self):
        print("添加顺时针1圈指令到命令队列")
        arr = 1000
        pcnt =   64   # 64细分
        for i in range(600):
            self.serial.cmd_queue_put((arr, pcnt, 0, arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0))
        
        #添加启动指令
        #arr = 65535*10
        #pcnt = 0
        #pen = 0
        #self.serial.cmd_queue_put((arr, pcnt, pen, arr, pcnt, pen, arr, pcnt, pen, arr, pcnt, pen))
        
        print(f'队列指令数量 {self.serial.cmd_queue.qsize()}')
        
    # 添加逆时针1圈指令
    def pbAppendCCWCmd_clicked(self):
        print("添加逆时针1圈指令到命令队列")
        arr = 1200
        pcnt = -200 * 64   # 64细分
        self.serial.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 1, arr, pcnt, 1, arr, pcnt, 1))
        #添加启动指令
        arr = 65535*10
        self.serial.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 1, arr, pcnt, 1, arr, pcnt, 1))
        print(f'队列指令数量 {self.serial.cmd_queue.qsize()}')
        
    # 队列指令同步到控制器
    def pbCmdQueueSync_clicked(self):
        print("队列指令同步到控制器")
        self.serial.cmd_queue_sync()
    
    # 添加电机停止命令到命令队列
    def pbStop_clicked(self):
        a1 = 655350            # arr大于65535，发送队列命令时会替换成电机启动命令
        p1 = 0
        e1 = 0
        a2 = 655350
        p2 = 0
        e2 = 0            
        a3 = 655350
        p3 = 0
        e3 = 0            
        a4 = 655350
        p4 = 0
        e4 = 0
        cmd_motor_stop = (a1, p1, e1, a2, p2, e2, a3, p3, e3, a4, p4, e4)
        print('添加电机停止命令 - ', cmd_motor_stop)
        self.serial.cmd_queue_put(cmd_motor_stop)  # 添加命令到缓冲区        
        print('命令缓冲区中命令数量 = ', self.serial.cmd_queue.qsize())

    # 添加命令到命令队列
    def pbAppendCmd_clicked(self):
        cmd_cnt = int(self.cmdCntInput.currentText())
        print("添加命令数量=", cmd_cnt)
        for i in range(cmd_cnt):
            a1 = int(self.arr1Input.currentText())
            p1 = int(self.pcnt1Input.currentText())
            e1 = int(self.pen1Input.currentText())
            a2 = int(self.arr2Input.currentText())
            p2 = int(self.pcnt2Input.currentText())
            e2 = int(self.pen2Input.currentText())            
            a3 = int(self.arr3Input.currentText())
            p3 = int(self.pcnt3Input.currentText())
            e3 = int(self.pen3Input.currentText())
            a4 = int(self.arr4Input.currentText())
            p4 = int(self.pcnt4Input.currentText())
            e4 = int(self.pen4Input.currentText())            
            cmd = (a1, p1, e1, a2, p2, e2, a3, p3, e3, a4, p4, e4)
            print('添加命令 - ', cmd)
            self.serial.cmd_queue_put(cmd)  # 添加命令到缓冲区
        print('命令缓冲区中命令数量 = ', self.serial.cmd_queue.qsize())

    # 发送队列中命令到控制器
    def pbCmdSend_clicked(self):
        print('发送队列中命令到控制')

    # 广播停机
    def pbAllStop_clicked(self):
        self.serial.all_motor_stop()
    
    # 清除编码器计数值
    def encoder_clear_clicked(self):
        self.serial.pos
        print('encoder value clear')

    # 串口打开关闭
    def pbUartOpen_clicked(self):
        # 如果没有可用串口，则刷新系统串口列表
        if self.cbUartPort.currentText() == "":
            Update_Serial(self.serial, self.cbUartPort)
            return

        if self.pbUartOpen.text() == "打开串口":
            port = self.cbUartPort.currentText()
            uart_cfg = [port, 115200]
            Save_Uart_Cfg(uart_cfg)              # 保存串口配置参数

            if not self.serial.open_port(port):
                self.msgbox_show(info="打开串口出错")
                return

            self.pbUartOpen.setText("关闭串口")

           # 广播指令，读设备地址
            adr = self.serial.read_dev_adr()
            print('dev adr:', adr)
            self.setCbIndex(str(adr), self.devAdr)   # 设置电机地址选择下拉框内容
            adr = int(self.devAdr.currentText())   # motor address: 1-20
            time.sleep(0.5)                             # 向驱动器发送连续指令必须有延时
            msg = self.serial.read_dev_msg()            # 读设备信息验证是否可连接
            if msg:
                print(msg)
                self.uartMsg.clear()
                self.uartMsg.append(f"驱动器{adr}已连接")
            
        else:
            self.serial.close_port()
            self.pbUartOpen.setText("打开串口")
            self.gbDevice.setTitle("驱动器 - 未连接")
            self.uartMsg.clear()

    # 写设备地址
    def pbWriteDevAdr_clicked(self):
        adr = int(self.devAdr.currentText())   # motor address: 1-20
        self.serial.write_dev_adr(adr)
        self.pbUartOpen_clicked()
        time.sleep(0.5)
        self.pbUartOpen_clicked()

    # 电机启动获取参数
    def get_pulse_para(self):

        adr = int(self.devAdr.currentText())   # motor address: 1-20
        rt = int(self.run_spd.currentText())     # speed
        
        pulse_cnt = int(self.m1_pulse_cnt.currentText())   # pulse sum
        arr = int(rt * self.clock / abs(pulse_cnt))
        pen = 1
        self.serial.adr = adr                           # set motor address
        self.serial.motor_run((arr, pulse_cnt, pen))    # send command
        
        print('motor run:', adr,arr, pulse_cnt, pen)

    # 启动控制器缓冲区命令运行
    def pbCmdRun_clicked(self):
        print("启动控制器缓冲区命令运行")
        self.serial.cmd_run_start()


    # Timer timeout event, 系统时间显示        
    def timer_out_func(self):
        lt = time.localtime()

        if None and self.serial.serPort is not None:
            # 发送指令读取编码器信息，显示在对话框
            if lt.tm_sec % 2:
                cnt = self.serial.read_encoder_counter()
                cnt_txt = "{:02d}".format(cnt)
                self.encoder_cnt.setText(cnt_txt)

            else:
                sw = self.serial.read_limit_sw()
                if sw: sw_txt = "OFF"
                else:  sw_txt = "ON"
                self.lmt_sw.setText(sw_txt)
        
        dt_str = "{:02d}:{:02d}:{:02d} {}-{:02d}-{:02d} ".format(lt.tm_hour, lt.tm_min, lt.tm_sec, lt.tm_year, lt.tm_mon, lt.tm_mday)
        wday_str = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
        self.label_datetime.setText("     "+dt_str + wday_str[lt.tm_wday])
        self.nowx.setText(str(self.serial.x0))
        self.nowy.setText(str(self.serial.y0))
        self.nowz.setText(str(self.serial.z0))

    # Exit Applicaiton
    def pbExit_clicked(self):
        # release source
        QApplication.quit()

    # 给定显示内容设置comboBox Index
    def setCbIndex(self, text, cb):
        if cb.findText(text) == -1:
            cb.addItem(text)     
        for n in range(cb.count()):
            if cb.itemText(n) == text:
                cb.setCurrentIndex(n)

