import sys
import random
from ctypes import *
import serial
from cmd_test_ui  import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow


port = ''
cmd = bytes
class UartThread(QThread):
    r'''uart function ,this class is used in writing attributes to usb
    '''
    trigger = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(UartThread,self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        global cmd
        global port

        with serial.Serial(port=port,baudrate=115200,timeout=0.1) as ser:
            ser.write(cmd)
            ACK = ser.readlines()

        if len(ACK)==0:
            ACK = "NO ACK"
        else:
            ACK = str(ACK)
        self.trigger.emit({"ACK":ACK})

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.init_option()

    def init_option(self):
        r'''初始化UI操作逻辑
        '''
        self.SendCMD.clicked.connect(self.button_click)

        self.thread = UartThread(self)
        self.thread.trigger.connect(self.uart_ACK_display)

    def button_click(self):
        r'''发送指令按钮回调函数
        '''
        try:
            global port,cmd
            content =self.CMDInput.toPlainText() #输入16进制表示的Unicode字符串,转换成对应的二进制数，保证命令内容在3Byte以内
            
            port = self.PortName.text() #获取串口设备名称
            
            cmdstr ,label,crc= self.cmd_pack(content)  #包装命令帧
            self.CRCDisplay.setText(crc)
            self.CMDLabelDisplay.setText(label)
            self.CMDBrowser.setText(cmdstr+"字节数:"+str(int(len(cmdstr)/2)))
            cmd = bytes.fromhex(cmdstr)
            #QApplication.processEvents()
            self.thread.start()
            self.SendCMD.setEnabled(False)
        except ValueError as v:
            self.ACKDisplay.setText("发生错误：{}".format(v))

    def uart_ACK_display(self,value:dict):
        self.ACKDisplay.setText(value["ACK"]+"字节数："+str(len(value["ACK"])))
        self.SendCMD.setEnabled(True)

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

    def cmd_pack(self,content:str)->str:

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
