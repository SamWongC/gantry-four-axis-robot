import sys
import time
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem,QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QTimer

from pyside6_app import AppPyside6

# scara机械臂控制程序
# 与AppPyside6程序共用ui界面
class AppScara(AppPyside6):

    def __init__(self, parent=None):
        super(AppScara, self).__init__()    
        # 执行点到点运动
        self.movep.clicked.connect(self.movep_clicked)

        # 执行直线运动
        self.movel.clicked.connect(self.movel_clicked)

        # 执行圆弧运动
        

        # 一键归位
        self.move0.clicked.connect(self.move0_clicked)

        # 左手模式 上三角
       # self.left.clicked.connect(self.left_clicked)
        
        # 右手模式 默认模式 下三角
       # self.right.clicked.connect(self.right_clicked)

        # z轴移动 最上方为零点
        self.movez.clicked.connect(self.movez_clicked)

        #选择文本文件并打开
        self.open_file.clicked.connect(self.openfile)

        self.movegcode.clicked.connect(self.movegcode_clicked)

    def left_clicked(self):
        self.left_right = 0

    def right_clicked(self):
        self.left_right = 1

    def moveq_clicked(self):
        self.moveq(self)
    
    def moveq(self):
        self.serial.parse_gcode()

    # movel
    def movel_clicked(self):
        startx = float(self.serial.x0)
        starty = float(self.serial.y0)
        endx = float(self.endx_L.currentText())
        endy = float(self.endy_L.currentText())
        self.serial.movel1(startx,starty,endx,endy)
        
    # movep
    def movep_clicked(self):
        startx = float(self.serial.x0)
        starty = float(self.serial.y0)
        endx = float(self.endx.currentText()) 
        endy = float(self.endy.currentText())
        self.serial.movep(startx,starty,endx,endy)
    
    # movez
    def movez_clicked(self):
        startz = float(self.serial.z0)
        endz   = float(self.endz.currentText())
        self.serial.movez(startz,endz)

    # move0
    def move0_clicked(self):
        self.serial.movep(self.serial.x0,self.serial.y0,self.serial.x00,self.serial.y00)
        self.serial.movez(self.serial.z0,self.serial.z00)
    
    def openfile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")

        # 如果用户选择了文件
        if file_name:
            self.file_path = file_name
            with open(file_name, 'r') as file:
                # 读取文件内容并显示在文本浏览器中
                self.gcode_browser.setText(file.read())
    
    def movegcode_clicked(self):
        self.serial.parse_gcode(self.file_path)


if __name__ == '__main__':

    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # Create and show the form
    app_dlg = AppScara()
     # 创建和显示都是在QWidget::show()内完成的
    # 在构造函数内获取QWidget的size()和几何尺寸，获取的总是不对
    # 构造函数结束时，窗口其实还没有创建，窗口尺寸尚未正式被设置
    app_dlg.show()
    sys.exit(app.exec())

