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
        MainWindow.resize(953, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CMDInput = QtWidgets.QTextEdit(self.centralwidget)
        self.CMDInput.setGeometry(QtCore.QRect(120, 140, 151, 41))
        self.CMDInput.setObjectName("CMDInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 61, 21))
        self.label.setObjectName("label")
        self.SendCMDButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendCMDButton.setGeometry(QtCore.QRect(180, 380, 75, 31))
        self.SendCMDButton.setObjectName("SendCMDButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 250, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 131, 16))
        self.label_3.setObjectName("label_3")
        self.ACKDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.ACKDisplay.setGeometry(QtCore.QRect(310, 100, 151, 111))
        self.ACKDisplay.setObjectName("ACKDisplay")
        self.CRCDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.CRCDisplay.setGeometry(QtCore.QRect(120, 250, 151, 31))
        self.CRCDisplay.setObjectName("CRCDisplay")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 61, 31))
        self.label_4.setObjectName("label_4")
        self.CMDLabelDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.CMDLabelDisplay.setGeometry(QtCore.QRect(120, 200, 151, 31))
        self.CMDLabelDisplay.setObjectName("CMDLabelDisplay")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 51, 31))
        self.label_5.setObjectName("label_5")
        self.CMDBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.CMDBrowser.setGeometry(QtCore.QRect(120, 300, 151, 71))
        self.CMDBrowser.setObjectName("CMDBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 30, 61, 21))
        self.label_6.setObjectName("label_6")
        self.PortName = QtWidgets.QLineEdit(self.centralwidget)
        self.PortName.setGeometry(QtCore.QRect(400, 50, 41, 21))
        self.PortName.setObjectName("PortName")
        self.CMDTypeBox = QtWidgets.QComboBox(self.centralwidget)
        self.CMDTypeBox.setGeometry(QtCore.QRect(120, 30, 81, 21))
        self.CMDTypeBox.setObjectName("CMDTypeBox")
        self.CMDTypeBox.addItem("")
        self.CMDTypeBox.addItem("")
        self.CMDTypeBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 150, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 230, 111, 16))
        self.label_8.setObjectName("label_8")
        self.ACKParserWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.ACKParserWindow.setGeometry(QtCore.QRect(310, 250, 151, 121))
        self.ACKParserWindow.setObjectName("ACKParserWindow")
        self.SerialPortTypeBox = QtWidgets.QComboBox(self.centralwidget)
        self.SerialPortTypeBox.setGeometry(QtCore.QRect(320, 50, 71, 22))
        self.SerialPortTypeBox.setObjectName("SerialPortTypeBox")
        self.SerialPortTypeBox.addItem("")
        self.SerialPortTypeBox.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 30, 101, 16))
        self.label_9.setObjectName("label_9")
        self.MsgTypeBox = QtWidgets.QComboBox(self.centralwidget)
        self.MsgTypeBox.setGeometry(QtCore.QRect(510, 60, 81, 21))
        self.MsgTypeBox.setObjectName("MsgTypeBox")
        self.MsgTypeBox.addItem("")
        self.MsgTypeBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 160, 111, 31))
        self.label_10.setObjectName("label_10")
        self.DeviceAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.DeviceAddress.setGeometry(QtCore.QRect(640, 200, 81, 21))
        self.DeviceAddress.setObjectName("DeviceAddress")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(640, 30, 71, 21))
        self.label_11.setObjectName("label_11")
        self.SpaceNumBox = QtWidgets.QComboBox(self.centralwidget)
        self.SpaceNumBox.setGeometry(QtCore.QRect(640, 60, 69, 22))
        self.SpaceNumBox.setObjectName("SpaceNumBox")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.SpaceNumBox.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(640, 100, 81, 21))
        self.label_12.setObjectName("label_12")
        self.SensorNumBox = QtWidgets.QComboBox(self.centralwidget)
        self.SensorNumBox.setGeometry(QtCore.QRect(640, 130, 69, 22))
        self.SensorNumBox.setObjectName("SensorNumBox")
        self.SensorNumBox.addItem("")
        self.SensorNumBox.addItem("")
        self.SensorNumBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(510, 100, 61, 16))
        self.label_13.setObjectName("label_13")
        self.SensorTypeBox = QtWidgets.QComboBox(self.centralwidget)
        self.SensorTypeBox.setGeometry(QtCore.QRect(510, 130, 91, 21))
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
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(510, 170, 91, 16))
        self.label_14.setObjectName("label_14")
        self.SensorData = QtWidgets.QLineEdit(self.centralwidget)
        self.SensorData.setGeometry(QtCore.QRect(510, 200, 81, 20))
        self.SensorData.setObjectName("SensorData")
        self.SendMsgButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendMsgButton.setGeometry(QtCore.QRect(640, 350, 81, 31))
        self.SendMsgButton.setObjectName("SendMsgButton")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(510, 240, 71, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(510, 300, 51, 21))
        self.label_16.setObjectName("label_16")
        self.MsgflowDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.MsgflowDisplay.setGeometry(QtCore.QRect(590, 280, 131, 51))
        self.MsgflowDisplay.setObjectName("MsgflowDisplay")
        self.MsgCRCdisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.MsgCRCdisplay.setGeometry(QtCore.QRect(590, 230, 131, 31))
        self.MsgCRCdisplay.setObjectName("MsgCRCdisplay")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 90, 91, 21))
        self.label_17.setObjectName("label_17")
        self.CMD_Example = QtWidgets.QTextBrowser(self.centralwidget)
        self.CMD_Example.setGeometry(QtCore.QRect(150, 70, 121, 61))
        self.CMD_Example.setObjectName("CMD_Example")
        self.GenerateCMDButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateCMDButton.setGeometry(QtCore.QRect(70, 380, 71, 31))
        self.GenerateCMDButton.setObjectName("GenerateCMDButton")
        self.OpenPortButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenPortButton.setGeometry(QtCore.QRect(310, 380, 61, 31))
        self.OpenPortButton.setObjectName("OpenPortButton")
        self.GenerateMSGBuuton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateMSGBuuton.setGeometry(QtCore.QRect(510, 350, 81, 31))
        self.GenerateMSGBuuton.setObjectName("GenerateMSGBuuton")
        self.ClosePortButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClosePortButton.setGeometry(QtCore.QRect(400, 380, 61, 31))
        self.ClosePortButton.setObjectName("ClosePortButton")
        self.CleanOutPutButton = QtWidgets.QPushButton(self.centralwidget)
        self.CleanOutPutButton.setGeometry(QtCore.QRect(350, 420, 61, 31))
        self.CleanOutPutButton.setObjectName("CleanOutPutButton")
        self.SerialPortTypeBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.SerialPortTypeBox_2.setGeometry(QtCore.QRect(770, 50, 71, 22))
        self.SerialPortTypeBox_2.setObjectName("SerialPortTypeBox_2")
        self.SerialPortTypeBox_2.addItem("")
        self.SerialPortTypeBox_2.addItem("")
        self.OpenPortButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.OpenPortButton_2.setGeometry(QtCore.QRect(760, 380, 61, 31))
        self.OpenPortButton_2.setObjectName("OpenPortButton_2")
        self.ClosePortButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ClosePortButton_2.setGeometry(QtCore.QRect(850, 380, 61, 31))
        self.ClosePortButton_2.setObjectName("ClosePortButton_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(800, 30, 61, 21))
        self.label_18.setObjectName("label_18")
        self.ACKParserWindow_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ACKParserWindow_2.setGeometry(QtCore.QRect(760, 250, 151, 121))
        self.ACKParserWindow_2.setObjectName("ACKParserWindow_2")
        self.ACKDisplay_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ACKDisplay_2.setGeometry(QtCore.QRect(760, 100, 151, 111))
        self.ACKDisplay_2.setObjectName("ACKDisplay_2")
        self.PortName_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.PortName_2.setGeometry(QtCore.QRect(850, 50, 41, 21))
        self.PortName_2.setObjectName("PortName_2")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(770, 80, 131, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(780, 230, 111, 16))
        self.label_20.setObjectName("label_20")
        self.CleanOutPutButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.CleanOutPutButton_2.setGeometry(QtCore.QRect(800, 420, 61, 31))
        self.CleanOutPutButton_2.setObjectName("CleanOutPutButton_2")
        self.SerialSendCMDButton = QtWidgets.QPushButton(self.centralwidget)
        self.SerialSendCMDButton.setGeometry(QtCore.QRect(110, 420, 91, 31))
        self.SerialSendCMDButton.setObjectName("SerialSendCMDButton")
        self.SerialSendMSGButton = QtWidgets.QPushButton(self.centralwidget)
        self.SerialSendMSGButton.setGeometry(QtCore.QRect(570, 390, 91, 31))
        self.SerialSendMSGButton.setObjectName("SerialSendMSGButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(220, 30, 81, 20))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menumesh = QtWidgets.QMenu(self.menubar)
        self.menumesh.setObjectName("menumesh")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menumesh.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "指令类型"))
        self.SendCMDButton.setText(_translate("MainWindow", "发送指令"))
        self.label_2.setText(_translate("MainWindow", "CRC32校验码"))
        self.label_3.setText(_translate("MainWindow", "下位机信息比特流"))
        self.label_4.setText(_translate("MainWindow", "指令标签"))
        self.label_5.setText(_translate("MainWindow", "指令流"))
        self.label_6.setText(_translate("MainWindow", "串口设备名"))
        self.CMDTypeBox.setItemText(0, _translate("MainWindow", "时间同步"))
        self.CMDTypeBox.setItemText(1, _translate("MainWindow", "节点控制"))
        self.CMDTypeBox.setItemText(2, _translate("MainWindow", "信息获取"))
        self.label_7.setText(_translate("MainWindow", "指令内容"))
        self.label_8.setText(_translate("MainWindow", "下位机信息解码"))
        self.SerialPortTypeBox.setItemText(0, _translate("MainWindow", "COM"))
        self.SerialPortTypeBox.setItemText(1, _translate("MainWindow", "/dev/tty"))
        self.label_9.setText(_translate("MainWindow", "mesh信息类型"))
        self.MsgTypeBox.setItemText(0, _translate("MainWindow", "传感信息"))
        self.MsgTypeBox.setItemText(1, _translate("MainWindow", "路由信息"))
        self.label_10.setText(_translate("MainWindow", "设备内网地址(2By)"))
        self.label_11.setText(_translate("MainWindow", "空间编号"))
        self.SpaceNumBox.setItemText(0, _translate("MainWindow", "1"))
        self.SpaceNumBox.setItemText(1, _translate("MainWindow", "2"))
        self.SpaceNumBox.setItemText(2, _translate("MainWindow", "3"))
        self.SpaceNumBox.setItemText(3, _translate("MainWindow", "4"))
        self.SpaceNumBox.setItemText(4, _translate("MainWindow", "5"))
        self.label_12.setText(_translate("MainWindow", "传感器编号"))
        self.SensorNumBox.setItemText(0, _translate("MainWindow", "1"))
        self.SensorNumBox.setItemText(1, _translate("MainWindow", "2"))
        self.SensorNumBox.setItemText(2, _translate("MainWindow", "3"))
        self.label_13.setText(_translate("MainWindow", "传感器类型"))
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
        self.label_14.setText(_translate("MainWindow", "传感数据(2Byte)"))
        self.SendMsgButton.setText(_translate("MainWindow", "发送信息"))
        self.label_15.setText(_translate("MainWindow", "CRC校验码"))
        self.label_16.setText(_translate("MainWindow", "信息流"))
        self.label_17.setText(_translate("MainWindow", "指令内容示例"))
        self.GenerateCMDButton.setText(_translate("MainWindow", "生成指令"))
        self.OpenPortButton.setText(_translate("MainWindow", "打开串口"))
        self.GenerateMSGBuuton.setText(_translate("MainWindow", "生成信息"))
        self.ClosePortButton.setText(_translate("MainWindow", "关闭串口"))
        self.CleanOutPutButton.setText(_translate("MainWindow", "清理窗口"))
        self.SerialPortTypeBox_2.setItemText(0, _translate("MainWindow", "COM"))
        self.SerialPortTypeBox_2.setItemText(1, _translate("MainWindow", "/dev/tty"))
        self.OpenPortButton_2.setText(_translate("MainWindow", "打开串口"))
        self.ClosePortButton_2.setText(_translate("MainWindow", "关闭串口"))
        self.label_18.setText(_translate("MainWindow", "串口设备名"))
        self.label_19.setText(_translate("MainWindow", "下位机信息比特流"))
        self.label_20.setText(_translate("MainWindow", "下位机信息解码"))
        self.CleanOutPutButton_2.setText(_translate("MainWindow", "清理窗口"))
        self.SerialSendCMDButton.setText(_translate("MainWindow", "连续发送指令"))
        self.SerialSendMSGButton.setText(_translate("MainWindow", "连续发送信息"))
        self.checkBox.setText(_translate("MainWindow", "单机ACK"))
        self.menu.setTitle(_translate("MainWindow", "上位机模拟"))
        self.menumesh.setTitle(_translate("MainWindow", "mesh信息模拟"))

