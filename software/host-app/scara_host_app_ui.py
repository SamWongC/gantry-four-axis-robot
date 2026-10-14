# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scara_host_appvEQyJf.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1075, 641)
        Dialog.setMinimumSize(QSize(64, 24))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gbDevice = QGroupBox(self.frame_2)
        self.gbDevice.setObjectName(u"gbDevice")
        self.gbDevice.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(9)
        self.gbDevice.setFont(font2)
        self.gbDevice.setMouseTracking(False)
        self.gbDevice.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.gridLayout = QGridLayout(self.gbDevice)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.groupBox = QGroupBox(self.gbDevice)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 73, 32))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(64, 32))
        self.label_9.setMaximumSize(QSize(96, 32))
        self.endx = QComboBox(self.groupBox)
        self.endx.addItem("")
        self.endx.setObjectName(u"endx")
        self.endx.setGeometry(QRect(90, 20, 81, 32))
        self.endx.setMaximumSize(QSize(96, 16777215))
        self.endx.setEditable(True)
        self.endy = QComboBox(self.groupBox)
        self.endy.addItem("")
        self.endy.setObjectName(u"endy")
        self.endy.setGeometry(QRect(180, 20, 71, 32))
        self.endy.setMaximumSize(QSize(96, 16777215))
        self.endy.setEditable(True)
        self.movep = QPushButton(self.groupBox)
        self.movep.setObjectName(u"movep")
        self.movep.setGeometry(QRect(280, 20, 100, 32))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.movep.sizePolicy().hasHeightForWidth())
        self.movep.setSizePolicy(sizePolicy2)
        self.movep.setMinimumSize(QSize(100, 32))
        self.movep.setMaximumSize(QSize(96, 16777215))
        self.movep.setCursor(QCursor(Qt.PointingHandCursor))
        self.movep.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(127, 165, 127);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 73, 32))
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(64, 32))
        self.label_10.setMaximumSize(QSize(96, 32))
        self.endx_L = QComboBox(self.groupBox)
        self.endx_L.addItem("")
        self.endx_L.setObjectName(u"endx_L")
        self.endx_L.setGeometry(QRect(90, 60, 81, 32))
        self.endx_L.setMaximumSize(QSize(96, 16777215))
        self.endx_L.setEditable(True)
        self.endy_L = QComboBox(self.groupBox)
        self.endy_L.addItem("")
        self.endy_L.setObjectName(u"endy_L")
        self.endy_L.setGeometry(QRect(180, 60, 71, 32))
        self.endy_L.setMaximumSize(QSize(96, 16777215))
        self.endy_L.setEditable(True)
        self.movel = QPushButton(self.groupBox)
        self.movel.setObjectName(u"movel")
        self.movel.setGeometry(QRect(280, 60, 100, 32))
        sizePolicy2.setHeightForWidth(self.movel.sizePolicy().hasHeightForWidth())
        self.movel.setSizePolicy(sizePolicy2)
        self.movel.setMinimumSize(QSize(100, 32))
        self.movel.setMaximumSize(QSize(96, 16777215))
        self.movel.setCursor(QCursor(Qt.PointingHandCursor))
        self.movel.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(127, 165, 127);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 200, 71, 21))
        font3 = QFont()
        font3.setPointSize(13)
        self.label_11.setFont(font3)
        self.label_11.setMouseTracking(True)
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setMargin(0)
        self.label_11.setIndent(0)
        self.nowx = QLabel(self.groupBox)
        self.nowx.setObjectName(u"nowx")
        self.nowx.setGeometry(QRect(130, 200, 71, 21))
        self.nowx.setFont(font1)
        self.nowx.setMouseTracking(False)
        self.nowx.setTextFormat(Qt.PlainText)
        self.nowx.setMargin(0)
        self.nowx.setIndent(0)
        self.nowy = QLabel(self.groupBox)
        self.nowy.setObjectName(u"nowy")
        self.nowy.setGeometry(QRect(210, 200, 71, 21))
        self.nowy.setTextFormat(Qt.PlainText)
        self.nowy.setMargin(0)
        self.nowy.setIndent(0)
        self.move0 = QPushButton(self.groupBox)
        self.move0.setObjectName(u"move0")
        self.move0.setGeometry(QRect(280, 140, 100, 32))
        sizePolicy2.setHeightForWidth(self.move0.sizePolicy().hasHeightForWidth())
        self.move0.setSizePolicy(sizePolicy2)
        self.move0.setMinimumSize(QSize(100, 32))
        self.move0.setMaximumSize(QSize(96, 16777215))
        self.move0.setCursor(QCursor(Qt.PointingHandCursor))
        self.move0.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(127, 165, 127);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 100, 73, 32))
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(64, 32))
        self.label_13.setMaximumSize(QSize(96, 32))
        self.endz = QComboBox(self.groupBox)
        self.endz.addItem("")
        self.endz.setObjectName(u"endz")
        self.endz.setGeometry(QRect(90, 100, 81, 32))
        self.endz.setMaximumSize(QSize(96, 16777215))
        self.endz.setEditable(True)
        self.movez = QPushButton(self.groupBox)
        self.movez.setObjectName(u"movez")
        self.movez.setGeometry(QRect(280, 100, 100, 32))
        sizePolicy2.setHeightForWidth(self.movez.sizePolicy().hasHeightForWidth())
        self.movez.setSizePolicy(sizePolicy2)
        self.movez.setMinimumSize(QSize(100, 32))
        self.movez.setMaximumSize(QSize(96, 16777215))
        self.movez.setCursor(QCursor(Qt.PointingHandCursor))
        self.movez.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(127, 165, 127);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.open_file = QPushButton(self.groupBox)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setGeometry(QRect(420, 20, 100, 32))
        sizePolicy2.setHeightForWidth(self.open_file.sizePolicy().hasHeightForWidth())
        self.open_file.setSizePolicy(sizePolicy2)
        self.open_file.setMinimumSize(QSize(100, 32))
        self.open_file.setMaximumSize(QSize(96, 16777215))
        self.open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(127, 165, 127);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.movegcode = QPushButton(self.groupBox)
        self.movegcode.setObjectName(u"movegcode")
        self.movegcode.setGeometry(QRect(420, 60, 100, 32))
        sizePolicy2.setHeightForWidth(self.movegcode.sizePolicy().hasHeightForWidth())
        self.movegcode.setSizePolicy(sizePolicy2)
        self.movegcode.setMinimumSize(QSize(100, 32))
        self.movegcode.setMaximumSize(QSize(96, 16777215))
        self.movegcode.setCursor(QCursor(Qt.PointingHandCursor))
        self.movegcode.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(127, 165, 127);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.nowz = QLabel(self.groupBox)
        self.nowz.setObjectName(u"nowz")
        self.nowz.setGeometry(QRect(290, 200, 71, 21))
        self.nowz.setTextFormat(Qt.PlainText)
        self.nowz.setMargin(0)
        self.nowz.setIndent(0)
        self.gcode_browser = QTextBrowser(self.groupBox)
        self.gcode_browser.setObjectName(u"gcode_browser")
        self.gcode_browser.setGeometry(QRect(540, 20, 331, 161))

        self.gridLayout.addWidget(self.groupBox, 0, 1, 2, 1)

        self.groupBox_2 = QGroupBox(self.gbDevice)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 256))
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.arr1Input = QComboBox(self.groupBox_2)
        self.arr1Input.addItem("")
        self.arr1Input.addItem("")
        self.arr1Input.addItem("")
        self.arr1Input.addItem("")
        self.arr1Input.setObjectName(u"arr1Input")
        self.arr1Input.setGeometry(QRect(10, 70, 70, 28))
        self.arr1Input.setMinimumSize(QSize(70, 26))
        self.arr1Input.setMaximumSize(QSize(70, 28))
        self.arr1Input.setStyleSheet(u"background-color: rgb(200, 200,190);")
        self.arr1Input.setEditable(True)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 64, 24))
        self.label_2.setMinimumSize(QSize(64, 24))
        self.label_2.setMaximumSize(QSize(64, 24))
        self.label_2.setStyleSheet(u"color: rgb(120, 120, 0);")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 40, 64, 24))
        self.label_5.setMinimumSize(QSize(64, 24))
        self.label_5.setMaximumSize(QSize(64, 24))
        self.label_5.setStyleSheet(u"color: rgb(120, 120, 0);")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 40, 64, 24))
        self.label_7.setMinimumSize(QSize(64, 24))
        self.label_7.setMaximumSize(QSize(64, 24))
        self.label_7.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 130, 64, 24))
        self.label_6.setMinimumSize(QSize(64, 24))
        self.label_6.setMaximumSize(QSize(64, 24))
        self.label_6.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(330, 130, 64, 24))
        self.label_17.setMinimumSize(QSize(64, 24))
        self.label_17.setMaximumSize(QSize(64, 24))
        self.label_17.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(400, 130, 64, 24))
        self.label_18.setMinimumSize(QSize(64, 24))
        self.label_18.setMaximumSize(QSize(64, 24))
        self.label_18.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.arr3Input = QComboBox(self.groupBox_2)
        self.arr3Input.addItem("")
        self.arr3Input.addItem("")
        self.arr3Input.addItem("")
        self.arr3Input.addItem("")
        self.arr3Input.setObjectName(u"arr3Input")
        self.arr3Input.setGeometry(QRect(10, 160, 70, 28))
        self.arr3Input.setMinimumSize(QSize(70, 26))
        self.arr3Input.setMaximumSize(QSize(70, 28))
        self.arr3Input.setStyleSheet(u"background-color: rgb(200, 200,190);")
        self.arr3Input.setEditable(True)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 64, 24))
        self.label_3.setMinimumSize(QSize(64, 24))
        self.label_3.setMaximumSize(QSize(64, 24))
        self.label_3.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 130, 64, 24))
        self.label_8.setMinimumSize(QSize(64, 24))
        self.label_8.setMaximumSize(QSize(64, 24))
        self.label_8.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(240, 40, 64, 24))
        self.label_15.setMinimumSize(QSize(64, 24))
        self.label_15.setMaximumSize(QSize(64, 24))
        self.label_15.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(330, 40, 64, 24))
        self.label_14.setMinimumSize(QSize(64, 24))
        self.label_14.setMaximumSize(QSize(64, 24))
        self.label_14.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(400, 40, 64, 24))
        self.label_12.setMinimumSize(QSize(64, 24))
        self.label_12.setMaximumSize(QSize(64, 24))
        self.label_12.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.pen1Input = QComboBox(self.groupBox_2)
        self.pen1Input.addItem("")
        self.pen1Input.addItem("")
        self.pen1Input.setObjectName(u"pen1Input")
        self.pen1Input.setGeometry(QRect(170, 70, 48, 28))
        self.pen1Input.setMinimumSize(QSize(48, 26))
        self.pen1Input.setMaximumSize(QSize(64, 28))
        self.pen1Input.setEditable(True)
        self.arr2Input = QComboBox(self.groupBox_2)
        self.arr2Input.addItem("")
        self.arr2Input.addItem("")
        self.arr2Input.addItem("")
        self.arr2Input.addItem("")
        self.arr2Input.setObjectName(u"arr2Input")
        self.arr2Input.setGeometry(QRect(250, 70, 70, 28))
        self.arr2Input.setMinimumSize(QSize(70, 26))
        self.arr2Input.setMaximumSize(QSize(70, 28))
        self.arr2Input.setEditable(True)
        self.pcnt2Input = QComboBox(self.groupBox_2)
        self.pcnt2Input.addItem("")
        self.pcnt2Input.addItem("")
        self.pcnt2Input.addItem("")
        self.pcnt2Input.addItem("")
        self.pcnt2Input.setObjectName(u"pcnt2Input")
        self.pcnt2Input.setGeometry(QRect(330, 70, 70, 28))
        self.pcnt2Input.setMinimumSize(QSize(70, 26))
        self.pcnt2Input.setMaximumSize(QSize(70, 28))
        self.pcnt2Input.setEditable(True)
        self.pen2Input = QComboBox(self.groupBox_2)
        self.pen2Input.addItem("")
        self.pen2Input.addItem("")
        self.pen2Input.setObjectName(u"pen2Input")
        self.pen2Input.setGeometry(QRect(410, 70, 48, 26))
        self.pen2Input.setMinimumSize(QSize(48, 26))
        self.pen2Input.setMaximumSize(QSize(64, 28))
        self.pen2Input.setFont(font)
        self.pen2Input.setEditable(True)
        self.pen2Input.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.pcnt4Input = QComboBox(self.groupBox_2)
        self.pcnt4Input.addItem("")
        self.pcnt4Input.addItem("")
        self.pcnt4Input.addItem("")
        self.pcnt4Input.setObjectName(u"pcnt4Input")
        self.pcnt4Input.setGeometry(QRect(330, 160, 70, 28))
        self.pcnt4Input.setMinimumSize(QSize(70, 26))
        self.pcnt4Input.setMaximumSize(QSize(70, 28))
        self.pcnt4Input.setEditable(True)
        self.pen4Input = QComboBox(self.groupBox_2)
        self.pen4Input.addItem("")
        self.pen4Input.addItem("")
        self.pen4Input.setObjectName(u"pen4Input")
        self.pen4Input.setGeometry(QRect(410, 160, 48, 28))
        self.pen4Input.setMinimumSize(QSize(48, 26))
        self.pen4Input.setMaximumSize(QSize(64, 28))
        self.pen4Input.setEditable(True)
        self.pcnt3Input = QComboBox(self.groupBox_2)
        self.pcnt3Input.addItem("")
        self.pcnt3Input.addItem("")
        self.pcnt3Input.addItem("")
        self.pcnt3Input.addItem("")
        self.pcnt3Input.setObjectName(u"pcnt3Input")
        self.pcnt3Input.setGeometry(QRect(90, 160, 70, 28))
        self.pcnt3Input.setMinimumSize(QSize(70, 26))
        self.pcnt3Input.setMaximumSize(QSize(70, 28))
        self.pcnt3Input.setEditable(True)
        self.pcnt1Input = QComboBox(self.groupBox_2)
        self.pcnt1Input.addItem("")
        self.pcnt1Input.addItem("")
        self.pcnt1Input.addItem("")
        self.pcnt1Input.addItem("")
        self.pcnt1Input.setObjectName(u"pcnt1Input")
        self.pcnt1Input.setGeometry(QRect(90, 70, 70, 28))
        self.pcnt1Input.setMinimumSize(QSize(70, 26))
        self.pcnt1Input.setMaximumSize(QSize(70, 28))
        self.pcnt1Input.setStyleSheet(u"background-color: rgb(200, 200,190);")
        self.pcnt1Input.setEditable(True)
        self.pen3Input = QComboBox(self.groupBox_2)
        self.pen3Input.addItem("")
        self.pen3Input.addItem("")
        self.pen3Input.setObjectName(u"pen3Input")
        self.pen3Input.setGeometry(QRect(170, 160, 48, 28))
        self.pen3Input.setMinimumSize(QSize(48, 26))
        self.pen3Input.setMaximumSize(QSize(64, 28))
        self.pen3Input.setEditable(True)
        self.arr4Input = QComboBox(self.groupBox_2)
        self.arr4Input.addItem("")
        self.arr4Input.addItem("")
        self.arr4Input.addItem("")
        self.arr4Input.addItem("")
        self.arr4Input.setObjectName(u"arr4Input")
        self.arr4Input.setGeometry(QRect(250, 160, 70, 28))
        self.arr4Input.setMinimumSize(QSize(70, 26))
        self.arr4Input.setMaximumSize(QSize(70, 28))
        self.arr4Input.setEditable(True)
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(240, 130, 64, 24))
        self.label_16.setMinimumSize(QSize(64, 24))
        self.label_16.setMaximumSize(QSize(64, 24))
        self.label_16.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(480, 10, 171, 231))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 10, 96, 24))
        self.label_19.setMinimumSize(QSize(96, 24))
        self.label_19.setMaximumSize(QSize(96, 32))
        self.label_19.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.cmdCntInput = QComboBox(self.frame)
        self.cmdCntInput.addItem("")
        self.cmdCntInput.addItem("")
        self.cmdCntInput.addItem("")
        self.cmdCntInput.setObjectName(u"cmdCntInput")
        self.cmdCntInput.setGeometry(QRect(40, 40, 96, 26))
        self.cmdCntInput.setMinimumSize(QSize(96, 26))
        self.cmdCntInput.setMaximumSize(QSize(96, 26))
        self.cmdCntInput.setEditable(True)
        self.pbAppendCmd = QPushButton(self.frame)
        self.pbAppendCmd.setObjectName(u"pbAppendCmd")
        self.pbAppendCmd.setGeometry(QRect(40, 80, 100, 32))
        sizePolicy2.setHeightForWidth(self.pbAppendCmd.sizePolicy().hasHeightForWidth())
        self.pbAppendCmd.setSizePolicy(sizePolicy2)
        self.pbAppendCmd.setMinimumSize(QSize(100, 32))
        self.pbAppendCmd.setMaximumSize(QSize(96, 16777215))
        self.pbAppendCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbAppendCmd.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(0, 120, 120);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.pbStop = QPushButton(self.frame)
        self.pbStop.setObjectName(u"pbStop")
        self.pbStop.setGeometry(QRect(40, 130, 100, 32))
        sizePolicy2.setHeightForWidth(self.pbStop.sizePolicy().hasHeightForWidth())
        self.pbStop.setSizePolicy(sizePolicy2)
        self.pbStop.setMinimumSize(QSize(100, 32))
        self.pbStop.setMaximumSize(QSize(96, 16777215))
        self.pbStop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbStop.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(0, 120, 120);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.pbCmdSend = QPushButton(self.frame)
        self.pbCmdSend.setObjectName(u"pbCmdSend")
        self.pbCmdSend.setGeometry(QRect(40, 180, 100, 32))
        sizePolicy2.setHeightForWidth(self.pbCmdSend.sizePolicy().hasHeightForWidth())
        self.pbCmdSend.setSizePolicy(sizePolicy2)
        self.pbCmdSend.setMinimumSize(QSize(100, 32))
        self.pbCmdSend.setMaximumSize(QSize(96, 16777215))
        self.pbCmdSend.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbCmdSend.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(0, 120, 120);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 110, 451, 16))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pbAppendCWCmd = QPushButton(self.groupBox_2)
        self.pbAppendCWCmd.setObjectName(u"pbAppendCWCmd")
        self.pbAppendCWCmd.setGeometry(QRect(0, 210, 128, 32))
        sizePolicy2.setHeightForWidth(self.pbAppendCWCmd.sizePolicy().hasHeightForWidth())
        self.pbAppendCWCmd.setSizePolicy(sizePolicy2)
        self.pbAppendCWCmd.setMinimumSize(QSize(128, 32))
        self.pbAppendCWCmd.setMaximumSize(QSize(128, 16777215))
        self.pbAppendCWCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbAppendCWCmd.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(0, 120, 120);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.pbAppendCCWCmd = QPushButton(self.groupBox_2)
        self.pbAppendCCWCmd.setObjectName(u"pbAppendCCWCmd")
        self.pbAppendCCWCmd.setGeometry(QRect(160, 210, 128, 32))
        sizePolicy2.setHeightForWidth(self.pbAppendCCWCmd.sizePolicy().hasHeightForWidth())
        self.pbAppendCCWCmd.setSizePolicy(sizePolicy2)
        self.pbAppendCCWCmd.setMinimumSize(QSize(128, 32))
        self.pbAppendCCWCmd.setMaximumSize(QSize(128, 16777215))
        self.pbAppendCCWCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbAppendCCWCmd.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(0, 120, 120);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.pbCmdQueueSync = QPushButton(self.groupBox_2)
        self.pbCmdQueueSync.setObjectName(u"pbCmdQueueSync")
        self.pbCmdQueueSync.setGeometry(QRect(330, 210, 128, 32))
        sizePolicy2.setHeightForWidth(self.pbCmdQueueSync.sizePolicy().hasHeightForWidth())
        self.pbCmdQueueSync.setSizePolicy(sizePolicy2)
        self.pbCmdQueueSync.setMinimumSize(QSize(128, 32))
        self.pbCmdQueueSync.setMaximumSize(QSize(128, 16777215))
        self.pbCmdQueueSync.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbCmdQueueSync.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(0, 120, 120);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")

        self.gridLayout.addWidget(self.groupBox_2, 4, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.gbDevice)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(128, 256))
        self.groupBox_3.setMaximumSize(QSize(128, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, -1, -1, -1)
        self.encoder_clear = QPushButton(self.groupBox_3)
        self.encoder_clear.setObjectName(u"encoder_clear")
        sizePolicy2.setHeightForWidth(self.encoder_clear.sizePolicy().hasHeightForWidth())
        self.encoder_clear.setSizePolicy(sizePolicy2)
        self.encoder_clear.setMinimumSize(QSize(100, 32))
        self.encoder_clear.setMaximumSize(QSize(96, 16777215))
        self.encoder_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.encoder_clear.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(64, 128, 0);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")

        self.verticalLayout_2.addWidget(self.encoder_clear)

        self.encoder_clear_2 = QPushButton(self.groupBox_3)
        self.encoder_clear_2.setObjectName(u"encoder_clear_2")
        sizePolicy2.setHeightForWidth(self.encoder_clear_2.sizePolicy().hasHeightForWidth())
        self.encoder_clear_2.setSizePolicy(sizePolicy2)
        self.encoder_clear_2.setMinimumSize(QSize(100, 32))
        self.encoder_clear_2.setMaximumSize(QSize(96, 16777215))
        self.encoder_clear_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.encoder_clear_2.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(64, 128, 0);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")

        self.verticalLayout_2.addWidget(self.encoder_clear_2)

        self.pbGenerate_2 = QPushButton(self.groupBox_3)
        self.pbGenerate_2.setObjectName(u"pbGenerate_2")
        sizePolicy2.setHeightForWidth(self.pbGenerate_2.sizePolicy().hasHeightForWidth())
        self.pbGenerate_2.setSizePolicy(sizePolicy2)
        self.pbGenerate_2.setMinimumSize(QSize(100, 32))
        self.pbGenerate_2.setMaximumSize(QSize(96, 16777215))
        self.pbGenerate_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbGenerate_2.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(64, 128, 0);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")

        self.verticalLayout_2.addWidget(self.pbGenerate_2)

        self.pbCmdRun = QPushButton(self.groupBox_3)
        self.pbCmdRun.setObjectName(u"pbCmdRun")
        sizePolicy2.setHeightForWidth(self.pbCmdRun.sizePolicy().hasHeightForWidth())
        self.pbCmdRun.setSizePolicy(sizePolicy2)
        self.pbCmdRun.setMinimumSize(QSize(100, 32))
        self.pbCmdRun.setMaximumSize(QSize(96, 16777215))
        self.pbCmdRun.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbCmdRun.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(64, 128, 0);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")

        self.verticalLayout_2.addWidget(self.pbCmdRun)


        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.gbDevice)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(128, 16777215))
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 14, 100, 32))
        self.label.setMinimumSize(QSize(100, 32))
        self.label.setMaximumSize(QSize(100, 32))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(127, 127, 0);")
        self.cbUartPort = QComboBox(self.groupBox_4)
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.setObjectName(u"cbUartPort")
        self.cbUartPort.setGeometry(QRect(13, 56, 98, 30))
        sizePolicy2.setHeightForWidth(self.cbUartPort.sizePolicy().hasHeightForWidth())
        self.cbUartPort.setSizePolicy(sizePolicy2)
        self.cbUartPort.setMinimumSize(QSize(98, 30))
        self.cbUartPort.setStyleSheet(u"background-color: rgb(210, 210, 200);")
        self.cbUartPort.setIconSize(QSize(12, 16))
        self.pbUartOpen = QPushButton(self.groupBox_4)
        self.pbUartOpen.setObjectName(u"pbUartOpen")
        self.pbUartOpen.setGeometry(QRect(13, 96, 100, 32))
        sizePolicy2.setHeightForWidth(self.pbUartOpen.sizePolicy().hasHeightForWidth())
        self.pbUartOpen.setSizePolicy(sizePolicy2)
        self.pbUartOpen.setMinimumSize(QSize(100, 32))
        self.pbUartOpen.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbUartOpen.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(64, 128, 0);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.uartMsg = QTextBrowser(self.groupBox_4)
        self.uartMsg.setObjectName(u"uartMsg")
        self.uartMsg.setGeometry(QRect(13, 138, 98, 64))
        self.uartMsg.setMinimumSize(QSize(60, 48))
        self.uartMsg.setMaximumSize(QSize(98, 64))
        self.uartMsg.setStyleSheet(u"color: rgb(127, 127, 0);\n"
"background-color: rgb(210, 210, 200);")
        self.uartMsg.setFrameShape(QFrame.NoFrame)
        self.devAdr = QComboBox(self.groupBox_4)
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.addItem("")
        self.devAdr.setObjectName(u"devAdr")
        self.devAdr.setGeometry(QRect(13, 212, 98, 30))
        self.devAdr.setMinimumSize(QSize(98, 30))
        self.devAdr.setMaximumSize(QSize(100, 16777215))
        self.devAdr.setStyleSheet(u"background-color: rgb(210, 210, 200);")
        self.devAdr.setEditable(True)
        self.pbWriteDevAdr = QPushButton(self.groupBox_4)
        self.pbWriteDevAdr.setObjectName(u"pbWriteDevAdr")
        self.pbWriteDevAdr.setGeometry(QRect(13, 252, 100, 32))
        sizePolicy2.setHeightForWidth(self.pbWriteDevAdr.sizePolicy().hasHeightForWidth())
        self.pbWriteDevAdr.setSizePolicy(sizePolicy2)
        self.pbWriteDevAdr.setMinimumSize(QSize(100, 32))
        self.pbWriteDevAdr.setMaximumSize(QSize(96, 16777215))
        self.pbWriteDevAdr.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbWriteDevAdr.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(205, 205, 205);\n"
"  background-color: rgb(64, 128, 0);\n"
"  border-radius: 4px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")

        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 2, 1)


        self.horizontalLayout_3.addWidget(self.gbDevice)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 20, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_datetime = QLabel(self.frame_3)
        self.label_datetime.setObjectName(u"label_datetime")

        self.horizontalLayout_2.addWidget(self.label_datetime)

        self.pbExit = QPushButton(self.frame_3)
        self.pbExit.setObjectName(u"pbExit")
        sizePolicy2.setHeightForWidth(self.pbExit.sizePolicy().hasHeightForWidth())
        self.pbExit.setSizePolicy(sizePolicy2)
        self.pbExit.setMinimumSize(QSize(96, 32))
        self.pbExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbExit.setStyleSheet(u"QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(154, 154, 154);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(127, 0, 20); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}")
        self.pbExit.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pbExit)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gbDevice.setTitle("")
        self.groupBox.setTitle("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"MOVEP", None))
        self.endx.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))

        self.endx.setCurrentText(QCoreApplication.translate("Dialog", u"0", None))
        self.endy.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))

        self.movep.setText(QCoreApplication.translate("Dialog", u"MOVEP", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"MOVEL", None))
        self.endx_L.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))

        self.endx_L.setCurrentText(QCoreApplication.translate("Dialog", u"0", None))
        self.endy_L.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))

        self.endy_L.setCurrentText(QCoreApplication.translate("Dialog", u"0", None))
        self.movel.setText(QCoreApplication.translate("Dialog", u"MOVEL", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u5750\u6807", None))
        self.nowx.setText("")
        self.nowy.setText("")
        self.move0.setText(QCoreApplication.translate("Dialog", u"MOVE0", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"MOVEZ", None))
        self.endz.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))

        self.endz.setCurrentText(QCoreApplication.translate("Dialog", u"0", None))
        self.movez.setText(QCoreApplication.translate("Dialog", u"MOVEZ", None))
        self.open_file.setText(QCoreApplication.translate("Dialog", u"Open File", None))
        self.movegcode.setText(QCoreApplication.translate("Dialog", u"MOVEG", None))
        self.nowz.setText("")
        self.groupBox_2.setTitle("")
        self.arr1Input.setItemText(0, QCoreApplication.translate("Dialog", u"500", None))
        self.arr1Input.setItemText(1, QCoreApplication.translate("Dialog", u"300", None))
        self.arr1Input.setItemText(2, QCoreApplication.translate("Dialog", u"800", None))
        self.arr1Input.setItemText(3, QCoreApplication.translate("Dialog", u"1000", None))

        self.arr1Input.setCurrentText(QCoreApplication.translate("Dialog", u"500", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ARR1", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"PCNT1", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"PEN1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"PCNT3", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"PCNT4", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"PEN4", None))
        self.arr3Input.setItemText(0, QCoreApplication.translate("Dialog", u"200", None))
        self.arr3Input.setItemText(1, QCoreApplication.translate("Dialog", u"100", None))
        self.arr3Input.setItemText(2, QCoreApplication.translate("Dialog", u"500", None))
        self.arr3Input.setItemText(3, QCoreApplication.translate("Dialog", u"1000", None))

        self.arr3Input.setCurrentText(QCoreApplication.translate("Dialog", u"200", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"ARR3", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"PEN3", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"ARR2", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"PCNT2", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"PEN2", None))
        self.pen1Input.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.pen1Input.setItemText(1, QCoreApplication.translate("Dialog", u"0", None))

        self.pen1Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pen1Input.setCurrentText(QCoreApplication.translate("Dialog", u"1", None))
        self.arr2Input.setItemText(0, QCoreApplication.translate("Dialog", u"200", None))
        self.arr2Input.setItemText(1, QCoreApplication.translate("Dialog", u"100", None))
        self.arr2Input.setItemText(2, QCoreApplication.translate("Dialog", u"500", None))
        self.arr2Input.setItemText(3, QCoreApplication.translate("Dialog", u"1000", None))

        self.arr2Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.arr2Input.setCurrentText(QCoreApplication.translate("Dialog", u"200", None))
        self.pcnt2Input.setItemText(0, QCoreApplication.translate("Dialog", u"128", None))
        self.pcnt2Input.setItemText(1, QCoreApplication.translate("Dialog", u"1280", None))
        self.pcnt2Input.setItemText(2, QCoreApplication.translate("Dialog", u"2560", None))
        self.pcnt2Input.setItemText(3, QCoreApplication.translate("Dialog", u"5120", None))

        self.pcnt2Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pcnt2Input.setCurrentText(QCoreApplication.translate("Dialog", u"128", None))
        self.pen2Input.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.pen2Input.setItemText(1, QCoreApplication.translate("Dialog", u"0", None))

        self.pen2Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pen2Input.setCurrentText(QCoreApplication.translate("Dialog", u"1", None))
        self.pcnt4Input.setItemText(0, QCoreApplication.translate("Dialog", u"128", None))
        self.pcnt4Input.setItemText(1, QCoreApplication.translate("Dialog", u"1280", None))
        self.pcnt4Input.setItemText(2, QCoreApplication.translate("Dialog", u"2560", None))

        self.pcnt4Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pcnt4Input.setCurrentText(QCoreApplication.translate("Dialog", u"128", None))
        self.pen4Input.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.pen4Input.setItemText(1, QCoreApplication.translate("Dialog", u"0", None))

        self.pen4Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pen4Input.setCurrentText(QCoreApplication.translate("Dialog", u"1", None))
        self.pcnt3Input.setItemText(0, QCoreApplication.translate("Dialog", u"128", None))
        self.pcnt3Input.setItemText(1, QCoreApplication.translate("Dialog", u"1280", None))
        self.pcnt3Input.setItemText(2, QCoreApplication.translate("Dialog", u"2560", None))
        self.pcnt3Input.setItemText(3, QCoreApplication.translate("Dialog", u"5120", None))

        self.pcnt3Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pcnt3Input.setCurrentText(QCoreApplication.translate("Dialog", u"128", None))
        self.pcnt1Input.setItemText(0, QCoreApplication.translate("Dialog", u"128", None))
        self.pcnt1Input.setItemText(1, QCoreApplication.translate("Dialog", u"1280", None))
        self.pcnt1Input.setItemText(2, QCoreApplication.translate("Dialog", u"2560", None))
        self.pcnt1Input.setItemText(3, QCoreApplication.translate("Dialog", u"5120", None))

        self.pcnt1Input.setCurrentText(QCoreApplication.translate("Dialog", u"128", None))
        self.pen3Input.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.pen3Input.setItemText(1, QCoreApplication.translate("Dialog", u"0", None))

        self.pen3Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.pen3Input.setCurrentText(QCoreApplication.translate("Dialog", u"1", None))
        self.arr4Input.setItemText(0, QCoreApplication.translate("Dialog", u"200", None))
        self.arr4Input.setItemText(1, QCoreApplication.translate("Dialog", u"100", None))
        self.arr4Input.setItemText(2, QCoreApplication.translate("Dialog", u"500", None))
        self.arr4Input.setItemText(3, QCoreApplication.translate("Dialog", u"1000", None))

        self.arr4Input.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: rgb(200, 200,190);", None))
        self.arr4Input.setCurrentText(QCoreApplication.translate("Dialog", u"200", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"ARR4", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u547d\u4ee4\u6dfb\u52a0\u6570\u91cf", None))
        self.cmdCntInput.setItemText(0, QCoreApplication.translate("Dialog", u"10", None))
        self.cmdCntInput.setItemText(1, QCoreApplication.translate("Dialog", u"50", None))
        self.cmdCntInput.setItemText(2, QCoreApplication.translate("Dialog", u"100", None))

        self.cmdCntInput.setCurrentText(QCoreApplication.translate("Dialog", u"10", None))
        self.pbAppendCmd.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u8fd0\u884c\u547d\u4ee4", None))
        self.pbStop.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u505c\u6b62\u547d\u4ee4", None))
        self.pbCmdSend.setText(QCoreApplication.translate("Dialog", u"\u53d1\u9001\u961f\u5217\u547d\u4ee4", None))
        self.pbAppendCWCmd.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u987a\u65f6\u94881\u5708\u6307\u4ee4", None))
        self.pbAppendCCWCmd.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u9006\u65f6\u94881\u5708\u6307\u4ee4", None))
        self.pbCmdQueueSync.setText(QCoreApplication.translate("Dialog", u"\u540c\u6b65\u6307\u4ee4\u5230\u7f13\u51b2\u533a", None))
        self.groupBox_3.setTitle("")
        self.encoder_clear.setText(QCoreApplication.translate("Dialog", u"\u6e05\u96f6\u7535\u673a\u4f4d\u7f6e", None))
        self.encoder_clear_2.setText(QCoreApplication.translate("Dialog", u"\u8bfb\u53d6\u7535\u673a\u4f4d\u7f6e", None))
        self.pbGenerate_2.setText(QCoreApplication.translate("Dialog", u"reserved", None))
        self.pbCmdRun.setText(QCoreApplication.translate("Dialog", u"\u542f\u52a8\u547d\u4ee4\u8fd0\u884c", None))
        self.groupBox_4.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4e32\u53e3\u540d\u79f0", None))
        self.cbUartPort.setItemText(0, QCoreApplication.translate("Dialog", u"com1", None))
        self.cbUartPort.setItemText(1, QCoreApplication.translate("Dialog", u"com2", None))
        self.cbUartPort.setItemText(2, QCoreApplication.translate("Dialog", u"com3", None))

        self.pbUartOpen.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u4e32\u53e3", None))
        self.devAdr.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.devAdr.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.devAdr.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))
        self.devAdr.setItemText(3, QCoreApplication.translate("Dialog", u"4", None))
        self.devAdr.setItemText(4, QCoreApplication.translate("Dialog", u"5", None))
        self.devAdr.setItemText(5, QCoreApplication.translate("Dialog", u"6", None))
        self.devAdr.setItemText(6, QCoreApplication.translate("Dialog", u"7", None))
        self.devAdr.setItemText(7, QCoreApplication.translate("Dialog", u"8", None))

        self.devAdr.setCurrentText(QCoreApplication.translate("Dialog", u"1", None))
        self.pbWriteDevAdr.setText(QCoreApplication.translate("Dialog", u"\u5199\u8bbe\u5907\u5730\u5740", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u54c8\u5c14\u6ee8\u5de5\u4e1a\u5927\u5b66\u673a\u7535\u63a7\u5236\u53ca\u81ea\u52a8\u5316\u7cfb", None))
        self.label_datetime.setText(QCoreApplication.translate("Dialog", u"2021-05-17", None))
        self.pbExit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa\u7a0b\u5e8f", None))
    # retranslateUi

