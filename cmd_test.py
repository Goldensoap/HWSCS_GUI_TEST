import sys
import random
import time
from ctypes import *
import serial
from cmd_test_ui  import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class UartThread(QThread):
    r'''uart function ,this class is used in writing attributes to usb
    '''
    trigger = pyqtSignal(dict)
    pipe = pyqtSignal(dict)

    def __init__(self,parent=None):
        super(UartThread,self).__init__()
        self.signal = False
        self.content = ''
        self.portName = ''
        self.pipe.connect(self.set_msg)

    def __del__(self):
        self.wait()

    def run(self):
        try:
            with serial.Serial(port=self.portName,baudrate=115200,timeout=0.1) as ser:
                while True:
                    if self.signal == "close": # 关闭信号，跳出循环结束线程
                        self.signal = False
                        break
                    elif self.signal == True: # 有发送内容，串口发送
                        ser.write(self.content)
                        self.signal = False
                    else: # 监听串口
                        ACK = ser.readline()
                        if len(ACK)!=0:
                            ACK = str(ACK)
                            self.trigger.emit({"ACK":ACK})

        except Exception as e:
            ACK ="发生错误：{}".format(e)
            self.trigger.emit({"ACK":ACK})

    def set_msg(self,value:dict):
        if "content" in value:
            self.content = value["content"]
        if "port" in value:
            self.portName = value["port"]
        if "signal" in value:
            self.signal = value["signal"]

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.init_option()
        self.cmd_type = "01" #时间同步
        self.port_type = "COM" #串口平台
        self.port_type_2 = "COM"
        self.msg_type = "01" #传感信息
        self.sensor_type = "01" #设备电量
        self.space_num = "01" #空间号
        self.sensor_num = "01" #传感器编号

    def init_option(self):
        r'''初始化UI操作逻辑
        '''
        self.GenerateCMDButton.clicked.connect(self.generate_cmd) #单纯生成命令以供查看和复制
        self.GenerateMSGBuuton.clicked.connect(self.generate_msg) #单纯生成信息以供查看和复制

        self.SendCMDButton.clicked.connect(self.send_cmd) # 发送命令
        self.SendCMDButton.setEnabled(False)
        self.SendMsgButton.clicked.connect(self.send_msg) # 发送模拟信息
        self.SendMsgButton.setEnabled(False)

        self.SerialPortTypeBox.activated.connect(self.select_port_type) # 串口类型选择
        self.SerialPortTypeBox_2.activated.connect(self.select_port_type_2)
        self.OpenPortButton.clicked.connect(self.open_port) #打开串口1
        self.ClosePortButton.clicked.connect(self.close_port) #关闭串口1
        self.ClosePortButton.setEnabled(False)
        self.OpenPortButton_2.clicked.connect(self.open_port_2) #打开串口2
        self.ClosePortButton_2.clicked.connect(self.close_port_2) #关闭串口2
        self.ClosePortButton_2.setEnabled(False)

        self.CleanOutPutButton.clicked.connect(self.clean_ack_windows) #清理窗口输出
        self.CleanOutPutButton_2.clicked.connect(self.clean_ack_windows_2)

        self.uart_port_work_thread = UartThread(self) #串口1收发工作线程
        self.uart_port_work_thread.trigger.connect(self.uart_ACK_display)
        self.uart_port_work_thread_2 = UartThread(self) #串口2收发工作线程
        self.uart_port_work_thread_2.trigger.connect(self.uart_ACK_display_2)

        
        self.CMDTypeBox.activated.connect(self.select_cmd_type) # 指令类型选择

        self.MsgTypeBox.activated.connect(self.select_msg_type) # 信息类型选择
        self.SensorTypeBox.activated.connect(self.select_sensor_type)# 传感器类型选择
        self.SensorNumBox.activated.connect(self.select_sensor_num)# 传感器编号选择
        self.SpaceNumBox.activated.connect(self.select_space_num)# 设备空间号选择

    def open_port(self):
        port = self.port_type+self.PortName.text() #获取串口设备名称
        self.uart_port_work_thread.pipe.emit({"port":port})
        self.uart_port_work_thread.start() # 开启串口1工作线程

        self.SendCMDButton.setEnabled(True)
        self.ClosePortButton.setEnabled(True)
        self.OpenPortButton.setEnabled(False)

    def close_port(self):
        self.uart_port_work_thread.pipe.emit({"signal":"close"})

        self.SendCMDButton.setEnabled(False)
        self.ClosePortButton.setEnabled(False)
        self.OpenPortButton.setEnabled(True)

    def open_port_2(self):
        port = self.port_type_2+self.PortName_2.text() #获取串口设备名称
        self.uart_port_work_thread_2.pipe.emit({"port":port})
        self.uart_port_work_thread_2.start() # 开启串口2工作线程

        self.SendMsgButton.setEnabled(True)
        self.ClosePortButton_2.setEnabled(True)
        self.OpenPortButton_2.setEnabled(False)

    def close_port_2(self):
        self.uart_port_work_thread_2.pipe.emit({"signal":"close"})

        self.SendMsgButton.setEnabled(False)
        self.ClosePortButton_2.setEnabled(False)
        self.OpenPortButton_2.setEnabled(True)

    def clean_ack_windows(self):
        self.ACKDisplay.setText("")
        self.ACKParserWindow.setText("")

    def clean_ack_windows_2(self):
        self.ACKDisplay_2.setText("")
        self.ACKParserWindow_2.setText("")

    def generate_cmd(self)->str:
        r'''根据UI选择和输入生成指令内容,并在UI相应位置显示。
        '''
        content =self.CMDInput.toPlainText() #输入16进制表示的Unicode字符串,转换成对应的二进制数

        #根据指令类型选择内容
        if self.cmd_type == "01" : 
            timestamp = format(int(time.time()),'x')
            content = self.cmd_type+timestamp
        else:
            content = self.cmd_type+content

        cmdstr ,label,crc= self.cmd_pack(content)  #包装命令帧

        self.CRCDisplay.setText(crc) # 在UI中显示相关内容
        self.CMDLabelDisplay.setText(label)
        self.CMDBrowser.setText(cmdstr+"字节数:"+str(int(len(cmdstr)/2)))

        return cmdstr

    def send_cmd(self):
        r'''发送指令按钮回调函数
        '''
        cmd = bytes.fromhex(self.generate_cmd())#获取指令内容,转换为二进制
        self.uart_port_work_thread.pipe.emit({"content":cmd,"signal":True})

    def generate_msg(self)->str:

        sensor_data = self.SensorData.text()
        device_address = self.DeviceAddress.text()
        #根据信息类型选择内容
        if self.msg_type == "01":
            content = self.msg_type+device_address+self.space_num+self.sensor_num+self.sensor_type+sensor_data
        elif self.msg_type == "02":
            content = ''

        msgstr,crc=self.msg_pack(content)

        self.MsgCRCdisplay.setText(crc) # 在UI中显示相关内容
        self.MsgflowDisplay.setText(msgstr+"字节数:"+str(int(len(msgstr)/2)))

        return msgstr

    def send_msg(self):
        r'''模拟mesh信息发送
        '''
        msg = bytes.fromhex(self.generate_msg())#获取信息内容，转换二进制
        self.uart_port_work_thread_2.pipe.emit({"content":msg,"signal":True})

    def select_msg_type(self):
        r'''选择mesh信息类型
        '''
        type_dict = {   
                        "传感信息":"01",
                        "路由信息":"02",
                    }
        self.msg_type = type_dict[self.MsgTypeBox.currentText()]

    def select_space_num(self):
        r'''选择终端所在空间号
        '''
        hexNum = format(int(self.SpaceNumBox.currentText()),'x')
        if (len(hexNum)%2) != 0:
            hexNum = '0'+hexNum
        self.space_num = hexNum

    def select_sensor_type(self):
        r'''选择传感器类型
        '''
        type_dict = {   
                "设备电量":"01",
                "光照":"02",
                "温度":"03",
                "湿度":"04",
                "人体红外":"05",
                "PM2.5":"06",
                "毒害气体":"07",
                "霍尔传感":"08",
                "电力线监测":"09",
                "CO2":"0A"
            }
        self.sensor_type =type_dict[self.SensorTypeBox.currentText()]

    def select_sensor_num(self):
        r'''选择传感器编号
        '''
        hexNum = format(int(self.SensorNumBox.currentText()),'x')
        if (len(hexNum)%2) != 0:
            hexNum = '0'+hexNum
        self.sensor_num = hexNum

    def select_cmd_type(self):
        r'''选择要发送的指令类型
        '''
        type_dict = {   
                        "时间同步":"01",
                        "节点控制":"02",
                        "信息获取":"03",
                    }

        self.cmd_type = type_dict[self.CMDTypeBox.currentText()]

    def select_port_type(self):
        r'''选择串口类型（windows/linux）
        '''
        self.port_type = self.SerialPortTypeBox.currentText()

    def select_port_type_2(self):
        r'''选择串口2类型（windows/linux）
        '''
        self.port_type_2 = self.SerialPortTypeBox_2.currentText()

    def uart_ACK_display(self,value:dict):
        r'''串口1信号回调函数
        '''
        self.ACKDisplay.append(value["ACK"]+"字节数："+str(len(value["ACK"])))

    def uart_ACK_display_2(self,value:dict):
        r'''串口2信号回调函数
        '''
        self.ACKDisplay_2.append(value["ACK"]+"字节数："+str(len(value["ACK"])))

    def crc_check(self,data:bytes)->str:
        r'''CRC校验函数
        '''
        crc32 = CDLL('libcrc32.dll')
        # 不足32位的，高位补0
        if len(data)%4 != 0:
            for i in range(int(4-len(data)%4)):
                data = bytes.fromhex('00')+data 
        
        _datalen = int(len(data)/4) # 计算数组长度
        DATASTR = c_uint * _datalen #创建C语言数组对象
        datastr = DATASTR()     #实例化数组
        for i in range(_datalen):
            num = (int(data[4*i])<<24)+(int(data[4*i+1])<<16)+(int(data[4*i+2])<<8)+int(data[4*i+3]) #字符串大端模式，还原uint
            datastr[_datalen-1-i]=num  #给数组赋值，采用小端模式
        CRC = crc32.cal_crc(datastr,_datalen) #计算CRC码，返回整数

        #还原8位无符号整数16进制形式
        if CRC < 0:
            CRC = 0x100000000+CRC
        CRC = format(CRC,'x')
        for i in range(8-len(CRC)):
            CRC = '0'+CRC

        return  CRC 

    def msg_pack(self,content:str)->str:
        r'''模拟mesh信息打包函数，负责校验和帧包装
        '''
        seq = content.split()
        temp = ''
        content = temp.join(seq) #去除空白符

        SOH = "01"
        EOT = "04"
        ESC = "1B"

        crc = self.crc_check(bytes.fromhex(content))
        msgstr = content+crc

        msg_bytes_list =[]
        for i in range(int(len(msgstr)/2)):
            msg_bytes_list.append(msgstr[2*i]+msgstr[2*i+1])
        #透明传输 转义字符填充（ESC 0X1B）
        for spc in msg_bytes_list:
            if spc in [SOH,EOT,ESC]:
                msg_bytes_list[msg_bytes_list.index(spc)] = ESC + spc  #字符填充

        final=''
        final =SOH+final.join(msg_bytes_list)+EOT
        return final,crc


    def cmd_pack(self,content:str)->str:
        r'''命令打包函数，负责校验，添加身份、标签，包装帧。
        '''
        seq = content.split()
        temp = ''
        content = temp.join(seq) #去除空白符

        SOH = "01"
        EOT = "04"
        ESC = "1B"
        identity = "00010203040506"

        label = format(random.randint(0,255),'x')
        if len(label) == 1:
            label = '0'+label
        #计算身份信息、指令内容、标签的CRC值
        crc = self.crc_check(bytes.fromhex(identity+content+label))
        #组合报文，并按字节分割，进行透传准备
        cmd = identity+content+label+crc
        cmd_bytes_list =[]
        for i in range(int(len(cmd)/2)):
            cmd_bytes_list.append(cmd[2*i]+cmd[2*i+1])
        #透明传输 转义字符填充（ESC 0X1B）
        for spc in cmd_bytes_list:
            if spc in [SOH,EOT,ESC]:
                cmd_bytes_list[cmd_bytes_list.index(spc)] = ESC + spc  #字符填充

        final=''
        final =SOH+final.join(cmd_bytes_list)+EOT
        return final, label, crc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
