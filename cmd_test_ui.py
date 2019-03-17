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
        MainWindow.resize(316, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CMDInput = QtWidgets.QTextEdit(self.centralwidget)
        self.CMDInput.setGeometry(QtCore.QRect(120, 30, 151, 31))
        self.CMDInput.setObjectName("CMDInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label.setObjectName("label")
        self.SendCMD = QtWidgets.QPushButton(self.centralwidget)
        self.SendCMD.setGeometry(QtCore.QRect(130, 120, 75, 23))
        self.SendCMD.setObjectName("SendCMD")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 350, 54, 12))
        self.label_3.setObjectName("label_3")
        self.ACKDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.ACKDisplay.setGeometry(QtCore.QRect(120, 340, 151, 31))
        self.ACKDisplay.setObjectName("ACKDisplay")
        self.CRCDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.CRCDisplay.setGeometry(QtCore.QRect(120, 160, 151, 31))
        self.CRCDisplay.setObjectName("CRCDisplay")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 54, 12))
        self.label_4.setObjectName("label_4")
        self.CMDLabelDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.CMDLabelDisplay.setGeometry(QtCore.QRect(120, 210, 151, 31))
        self.CMDLabelDisplay.setObjectName("CMDLabelDisplay")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 41, 21))
        self.label_5.setObjectName("label_5")
        self.CMDBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.CMDBrowser.setGeometry(QtCore.QRect(120, 250, 151, 71))
        self.CMDBrowser.setObjectName("CMDBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 61, 16))
        self.label_6.setObjectName("label_6")
        self.PortName = QtWidgets.QLineEdit(self.centralwidget)
        self.PortName.setGeometry(QtCore.QRect(120, 80, 151, 20))
        self.PortName.setObjectName("PortName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "指令输入"))
        self.SendCMD.setText(_translate("MainWindow", "发送指令"))
        self.label_2.setText(_translate("MainWindow", "CRC校验码"))
        self.label_3.setText(_translate("MainWindow", "下位机ACK"))
        self.label_4.setText(_translate("MainWindow", "指令标签"))
        self.label_5.setText(_translate("MainWindow", "指令流"))
        self.label_6.setText(_translate("MainWindow", "串口设备名"))

