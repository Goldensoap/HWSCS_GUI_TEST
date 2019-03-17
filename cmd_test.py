import sys
import random
from ctypes import *
import serial
from cmd_test_ui  import  *
from PyQt5.QtWidgets import QApplication, QMainWindow

class Uart:
    r'''uart function ,this class is used in writing attributes to usb
    '''
    def __init__(self,port:str):
        self._ser = serial.Serial(port=port,baudrate=115200,timeout=1)
    def port_write(self, command:bytes)->bool:
        r'''write ascii command to usb serial
        input parameters
            - command : the bytes type data 
        '''
        try:
            flag = False
            if self._ser.is_open != True:
                self._ser.open()
            self._ser.write(command)
        except serial.SerialException as s:
            pass
        except Exception as e:
            pass
        else:
            flag = True
        finally:
            return flag

    def port_read(self)->bytes:
        r'''read char type data from port
            return (bytes)info
        '''
        try:
            if self._ser.is_open != True:
                self._ser.open()
            info = self._ser.read(size=4)
        except serial.SerialException as s:
            pass
        except Exception as e:
            pass
        finally:
            return info

    def encode_int_hex_to_byte(self,numberList:list)->bytes:
        r'''
        input 0<= number =<255
        return hex str like 0d or f1
        '''
        hexStr = ''

        for number in numberList:
            hexNum = format(number,'x')
            if len(hexNum) == 1:
                hexNum = '0'+hexNum
            hexStr += hexNum

        char = bytes.fromhex(hexStr)

        return char

    def decode_byte_to_int(self,info:bytes)->list:
        r'''
        '''
        res = []
        for ele in info:
            res.append(int(ele))
        return res,len(res)


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.init_option()

    def init_option(self):
        r'''初始化UI操作逻辑
        '''
        self.SendCMD.clicked.connect(self.button_click)

    def button_click(self):
        r'''发送指令按钮回调函数
        '''
        content =self.CMDInput.toPlainText() #输入16进制表示的Unicode字符串,转换成对应的二进制数，保证命令内容在3Byte以内

        port = self.PortName.text() #获取串口设备名称

        cmd ,label,crc= self.cmd_pack(content)  #包装命令帧
        self.CRCDisplay.setText(crc)
        self.CMDLabelDisplay.setText(label)
        self.CMDBrowser.setText(cmd+"字节数:"+str(int(len(cmd)/2)))

        serial = Uart(port)
        serial.port_write(bytes.fromhex(cmd)) #发送命令

        ACK = serial.port_read() #等待ACK
        if len(ACK)==0:
            ACK = "NO ACK"
        self.ACKDisplay.setText(str(ACK)+"字节数："+str(len(ACK)))


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
