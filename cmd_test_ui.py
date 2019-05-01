# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ACKDisplay = QtWidgets.QTextBrowser(self.tab)
        self.ACKDisplay.setGeometry(QtCore.QRect(310, 120, 221, 91))
        self.ACKDisplay.setObjectName("ACKDisplay")
        self.CMDLabelDisplay = QtWidgets.QTextBrowser(self.tab)
        self.CMDLabelDisplay.setGeometry(QtCore.QRect(110, 180, 151, 31))
        self.CMDLabelDisplay.setObjectName("CMDLabelDisplay")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(310, 230, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(30, 70, 91, 21))
        self.label_17.setObjectName("label_17")
        self.ACKParserWindow = QtWidgets.QTextBrowser(self.tab)
        self.ACKParserWindow.setGeometry(QtCore.QRect(310, 260, 221, 121))
        self.ACKParserWindow.setObjectName("ACKParserWindow")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(330, 10, 61, 21))
        self.label_6.setObjectName("label_6")
        self.CleanOutPutButton = QtWidgets.QPushButton(self.tab)
        self.CleanOutPutButton.setGeometry(QtCore.QRect(310, 390, 71, 31))
        self.CleanOutPutButton.setObjectName("CleanOutPutButton")
        self.SerialPortTypeBox = QtWidgets.QComboBox(self.tab)
        self.SerialPortTypeBox.setGeometry(QtCore.QRect(312, 48, 69, 20))
        self.SerialPortTypeBox.setObjectName("SerialPortTypeBox")
        self.SerialPortTypeBox.addItem("")
        self.SerialPortTypeBox.addItem("")
        self.ACKcheck = QtWidgets.QCheckBox(self.tab)
        self.ACKcheck.setGeometry(QtCore.QRect(210, 10, 81, 20))
        self.ACKcheck.setObjectName("ACKcheck")
        self.PortName = QtWidgets.QLineEdit(self.tab)
        self.PortName.setGeometry(QtCore.QRect(387, 48, 39, 20))
        self.PortName.setObjectName("PortName")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 130, 61, 21))
        self.label_7.setObjectName("label_7")
        self.CRCDisplay = QtWidgets.QTextBrowser(self.tab)
        self.CRCDisplay.setGeometry(QtCore.QRect(110, 230, 151, 31))
        self.CRCDisplay.setObjectName("CRCDisplay")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 71, 31))
        self.label_2.setObjectName("label_2")
        self.CMDTypeBox = QtWidgets.QComboBox(self.tab)
        self.CMDTypeBox.setGeometry(QtCore.QRect(110, 10, 81, 21))
        self.CMDTypeBox.setObjectName("CMDTypeBox")
        self.CMDTypeBox.addItem("")
        self.CMDTypeBox.addItem("")
        self.CMDTypeBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(310, 90, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.label_4.setObjectName("label_4")
        self.CMDBrowser = QtWidgets.QTextBrowser(self.tab)
        self.CMDBrowser.setGeometry(QtCore.QRect(110, 280, 151, 71))
        self.CMDBrowser.setObjectName("CMDBrowser")
        self.CMDInput = QtWidgets.QTextEdit(self.tab)
        self.CMDInput.setGeometry(QtCore.QRect(110, 120, 151, 41))
        self.CMDInput.setObjectName("CMDInput")
        self.CMD_Example = QtWidgets.QTextBrowser(self.tab)
        self.CMD_Example.setGeometry(QtCore.QRect(140, 50, 121, 61))
        self.CMD_Example.setObjectName("CMD_Example")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(60, 360, 160, 56))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GenerateCMDButton = QtWidgets.QPushButton(self.widget)
        self.GenerateCMDButton.setObjectName("GenerateCMDButton")
        self.horizontalLayout.addWidget(self.GenerateCMDButton)
        self.SendCMDButton = QtWidgets.QPushButton(self.widget)
        self.SendCMDButton.setObjectName("SendCMDButton")
        self.horizontalLayout.addWidget(self.SendCMDButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.SerialSendCMDButton = QtWidgets.QPushButton(self.widget)
        self.SerialSendCMDButton.setObjectName("SerialSendCMDButton")
        self.verticalLayout.addWidget(self.SerialSendCMDButton)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(433, 31, 77, 54))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OpenPortButton = QtWidgets.QPushButton(self.widget1)
        self.OpenPortButton.setObjectName("OpenPortButton")
        self.verticalLayout_2.addWidget(self.OpenPortButton)
        self.ClosePortButton = QtWidgets.QPushButton(self.widget1)
        self.ClosePortButton.setObjectName("ClosePortButton")
        self.verticalLayout_2.addWidget(self.ClosePortButton)
        self.ACKcheck.raise_()
        self.ClosePortButton.raise_()
        self.ACKDisplay.raise_()
        self.CMDLabelDisplay.raise_()
        self.label.raise_()
        self.SendCMDButton.raise_()
        self.label_8.raise_()
        self.label_17.raise_()
        self.ACKParserWindow.raise_()
        self.label_6.raise_()
        self.CleanOutPutButton.raise_()
        self.OpenPortButton.raise_()
        self.SerialPortTypeBox.raise_()
        self.PortName.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.CRCDisplay.raise_()
        self.label_2.raise_()
        self.CMDTypeBox.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.SerialSendCMDButton.raise_()
        self.CMDBrowser.raise_()
        self.CMDInput.raise_()
        self.GenerateCMDButton.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ACKDisplay_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.ACKDisplay_2.setGeometry(QtCore.QRect(280, 90, 231, 91))
        self.ACKDisplay_2.setObjectName("ACKDisplay_2")
        self.SerialPortTypeBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.SerialPortTypeBox_2.setGeometry(QtCore.QRect(290, 40, 71, 22))
        self.SerialPortTypeBox_2.setObjectName("SerialPortTypeBox_2")
        self.SerialPortTypeBox_2.addItem("")
        self.SerialPortTypeBox_2.addItem("")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(320, 10, 61, 21))
        self.label_18.setObjectName("label_18")
        self.ACKParserWindow_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.ACKParserWindow_2.setGeometry(QtCore.QRect(280, 220, 231, 121))
        self.ACKParserWindow_2.setObjectName("ACKParserWindow_2")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 170, 71, 21))
        self.label_15.setObjectName("label_15")
        self.CleanOutPutButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.CleanOutPutButton_2.setGeometry(QtCore.QRect(280, 350, 61, 31))
        self.CleanOutPutButton_2.setObjectName("CleanOutPutButton_2")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(290, 70, 131, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(280, 190, 111, 16))
        self.label_20.setObjectName("label_20")
        self.MsgCRCdisplay = QtWidgets.QTextBrowser(self.tab_2)
        self.MsgCRCdisplay.setGeometry(QtCore.QRect(110, 170, 131, 31))
        self.MsgCRCdisplay.setObjectName("MsgCRCdisplay")
        self.PortName_2 = QtWidgets.QLineEdit(self.tab_2)
        self.PortName_2.setGeometry(QtCore.QRect(370, 40, 41, 21))
        self.PortName_2.setObjectName("PortName_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 240, 51, 21))
        self.label_16.setObjectName("label_16")
        self.MsgflowDisplay = QtWidgets.QTextBrowser(self.tab_2)
        self.MsgflowDisplay.setGeometry(QtCore.QRect(110, 230, 131, 51))
        self.MsgflowDisplay.setObjectName("MsgflowDisplay")
        self.widget2 = QtWidgets.QWidget(self.tab_2)
        self.widget2.setGeometry(QtCore.QRect(430, 20, 77, 54))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.OpenPortButton_2 = QtWidgets.QPushButton(self.widget2)
        self.OpenPortButton_2.setObjectName("OpenPortButton_2")
        self.verticalLayout_4.addWidget(self.OpenPortButton_2)
        self.ClosePortButton_2 = QtWidgets.QPushButton(self.widget2)
        self.ClosePortButton_2.setObjectName("ClosePortButton_2")
        self.verticalLayout_4.addWidget(self.ClosePortButton_2)
        self.widget3 = QtWidgets.QWidget(self.tab_2)
        self.widget3.setGeometry(QtCore.QRect(10, 20, 251, 128))
        self.widget3.setObjectName("widget3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.widget3)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget3)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.MsgTypeBox = QtWidgets.QComboBox(self.widget3)
        self.MsgTypeBox.setObjectName("MsgTypeBox")
        self.MsgTypeBox.addItem("")
        self.MsgTypeBox.addItem("")
        self.gridLayout.addWidget(self.MsgTypeBox, 1, 0, 1, 1)
        self.SpaceNumBox = QtWidgets.QComboBox(self.widget3)
        self.SpaceNumBox.setObjectName("SpaceNumBox")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.gridLayout.addWidget(self.SpaceNumBox, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget3)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.SensorTypeBox = QtWidgets.QComboBox(self.widget3)
        self.SensorTypeBox.setObjectName("SensorTypeBox")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.addItem("")
        self.SensorTypeBox.setItemText(10, "")
        self.gridLayout.addWidget(self.SensorTypeBox, 3, 0, 1, 1)
        self.SensorNumBox = QtWidgets.QComboBox(self.widget3)
        self.SensorNumBox.setObjectName("SensorNumBox")
        self.SensorNumBox.addItem("")
        self.SensorNumBox.addItem("")
        self.SensorNumBox.addItem("")
        self.gridLayout.addWidget(self.SensorNumBox, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget3)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget3)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 1, 1, 1)
        self.SensorData = QtWidgets.QLineEdit(self.widget3)
        self.SensorData.setObjectName("SensorData")
        self.gridLayout.addWidget(self.SensorData, 5, 0, 1, 1)
        self.DeviceAddress = QtWidgets.QLineEdit(self.widget3)
        self.DeviceAddress.setObjectName("DeviceAddress")
        self.gridLayout.addWidget(self.DeviceAddress, 5, 1, 1, 1)
        self.widget4 = QtWidgets.QWidget(self.tab_2)
        self.widget4.setGeometry(QtCore.QRect(50, 300, 160, 56))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GenerateMSGBuuton = QtWidgets.QPushButton(self.widget4)
        self.GenerateMSGBuuton.setObjectName("GenerateMSGBuuton")
        self.horizontalLayout_2.addWidget(self.GenerateMSGBuuton)
        self.SendMsgButton = QtWidgets.QPushButton(self.widget4)
        self.SendMsgButton.setObjectName("SendMsgButton")
        self.horizontalLayout_2.addWidget(self.SendMsgButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.SerialSendMSGButton = QtWidgets.QPushButton(self.widget4)
        self.SerialSendMSGButton.setObjectName("SerialSendMSGButton")
        self.verticalLayout_3.addWidget(self.SerialSendMSGButton)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "指令类型"))
        self.label_8.setText(_translate("MainWindow", "下位机信息解码"))
        self.label_17.setText(_translate("MainWindow", "指令内容示例"))
        self.label_6.setText(_translate("MainWindow", "串口设备名"))
        self.CleanOutPutButton.setText(_translate("MainWindow", "清理窗口"))
        self.SerialPortTypeBox.setItemText(0, _translate("MainWindow", "COM"))
        self.SerialPortTypeBox.setItemText(1, _translate("MainWindow", "/dev/tty"))
        self.ACKcheck.setText(_translate("MainWindow", "单机ACK"))
        self.label_5.setText(_translate("MainWindow", "指令流"))
        self.label_7.setText(_translate("MainWindow", "指令内容"))
        self.label_2.setText(_translate("MainWindow", "CRC32校验码"))
        self.CMDTypeBox.setItemText(0, _translate("MainWindow", "时间同步"))
        self.CMDTypeBox.setItemText(1, _translate("MainWindow", "节点控制"))
        self.CMDTypeBox.setItemText(2, _translate("MainWindow", "信息获取"))
        self.label_3.setText(_translate("MainWindow", "下位机信息比特流"))
        self.label_4.setText(_translate("MainWindow", "指令标签"))
        self.GenerateCMDButton.setText(_translate("MainWindow", "生成指令"))
        self.SendCMDButton.setText(_translate("MainWindow", "发送指令"))
        self.SerialSendCMDButton.setText(_translate("MainWindow", "连续发送指令"))
        self.OpenPortButton.setText(_translate("MainWindow", "打开串口"))
        self.ClosePortButton.setText(_translate("MainWindow", "关闭串口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "请求与指令测试"))
        self.SerialPortTypeBox_2.setItemText(0, _translate("MainWindow", "COM"))
        self.SerialPortTypeBox_2.setItemText(1, _translate("MainWindow", "/dev/tty"))
        self.label_18.setText(_translate("MainWindow", "串口设备名"))
        self.label_15.setText(_translate("MainWindow", "CRC校验码"))
        self.CleanOutPutButton_2.setText(_translate("MainWindow", "清理窗口"))
        self.label_19.setText(_translate("MainWindow", "下位机信息比特流"))
        self.label_20.setText(_translate("MainWindow", "下位机信息解码"))
        self.label_16.setText(_translate("MainWindow", "信息流"))
        self.OpenPortButton_2.setText(_translate("MainWindow", "打开串口"))
        self.ClosePortButton_2.setText(_translate("MainWindow", "关闭串口"))
        self.label_9.setText(_translate("MainWindow", "mesh信息类型"))
        self.label_11.setText(_translate("MainWindow", "空间编号"))
        self.MsgTypeBox.setItemText(0, _translate("MainWindow", "传感信息"))
        self.MsgTypeBox.setItemText(1, _translate("MainWindow", "路由信息"))
        self.SpaceNumBox.setItemText(0, _translate("MainWindow", "1"))
        self.SpaceNumBox.setItemText(1, _translate("MainWindow", "2"))
        self.SpaceNumBox.setItemText(2, _translate("MainWindow", "3"))
        self.SpaceNumBox.setItemText(3, _translate("MainWindow", "4"))
        self.SpaceNumBox.setItemText(4, _translate("MainWindow", "5"))
        self.label_13.setText(_translate("MainWindow", "传感器类型"))
        self.label_12.setText(_translate("MainWindow", "传感器编号"))
        self.SensorTypeBox.setItemText(0, _translate("MainWindow", "设备电量"))
        self.SensorTypeBox.setItemText(1, _translate("MainWindow", "光照"))
        self.SensorTypeBox.setItemText(2, _translate("MainWindow", "温度"))
        self.SensorTypeBox.setItemText(3, _translate("MainWindow", "湿度"))
        self.SensorTypeBox.setItemText(4, _translate("MainWindow", "人体红外"))
        self.SensorTypeBox.setItemText(5, _translate("MainWindow", "PM2.5"))
        self.SensorTypeBox.setItemText(6, _translate("MainWindow", "毒害气体"))
        self.SensorTypeBox.setItemText(7, _translate("MainWindow", "霍尔传感"))
        self.SensorTypeBox.setItemText(8, _translate("MainWindow", "电力线监测"))
        self.SensorTypeBox.setItemText(9, _translate("MainWindow", "CO2"))
        self.SensorNumBox.setItemText(0, _translate("MainWindow", "1"))
        self.SensorNumBox.setItemText(1, _translate("MainWindow", "2"))
        self.SensorNumBox.setItemText(2, _translate("MainWindow", "3"))
        self.label_14.setText(_translate("MainWindow", "传感数据(2Byte)"))
        self.label_10.setText(_translate("MainWindow", "设备内网地址(2By)"))
        self.GenerateMSGBuuton.setText(_translate("MainWindow", "生成信息"))
        self.SendMsgButton.setText(_translate("MainWindow", "发送信息"))
        self.SerialSendMSGButton.setText(_translate("MainWindow", "连续发送信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "模拟传感信息测试"))

