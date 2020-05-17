import sys
import time
import serial
import serial.tools.list_ports
from systemAPI import *
from cmd_test_ui  import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
import pyqtgraph as pg
import numpy as np


timec = 0
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
        global timec
        try:
            with serial.Serial(port=self.portName,baudrate=115200,timeout=0.1) as ser:
                while True:
                    if self.signal == "close": # 关闭信号，跳出循环结束线程
                        self.signal = False
                        break
                    elif self.signal == True: # 有发送内容，串口发送
                        timec = time.time()
                        ser.write(self.content)
                        self.signal = False
                    else: # 监听串口
                        ACK = ser.readline()
                        if len(ACK)!=0:
                            self.trigger.emit({"ACK":ACK,"Time":time.time()})

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

class UartPortCheckThread(QThread):

    trigger = pyqtSignal(list)
    def __init__(self,parent=None):
        super(UartPortCheckThread,self).__init__()
        self.portlist = []

    def run(self):
        while True:
            port = serial.tools.list_ports.comports()
            for i,element in enumerate(port):
                port[i] = element.device
            if port != self.portlist:
                self.portlist = port 
                self.trigger.emit(self.portlist)

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.list_num = 100
        self.graph=self.set_graph_ui()
        self.init_option()
        self.cmd_type = "01" #时间同步
        self.port = None #串口1
        self.port_2 = None #串口2
        self.msg_type = "01" #传感信息
        self.sensor_type = "01" #设备电量
        self.space_num = "01" #空间号
        self.sensor_num = "01" #传感器编号

        self.demo_space = {} #演示空间选项
        self.demo_display_space = None
        self.demo_data_table = {}#演示数据表
        self.timebase = 0  #演示时间基准

        self.now_select_sensor = None
        
        self.xdata_list = []

    def set_graph_ui(self):

        pg.setConfigOptions(antialias=True)
        win = pg.GraphicsLayoutWidget()
        self.graphLayout.addWidget(win)

        p = win.addPlot(title="传感器实时数据")
        p.setLabel('left', text='数值', color='#ffffff')
        p.setLabel('bottom', text='时间', units='s')
        p.setRange(xRange=[0,self.list_num-1],padding=0)
        p.showGrid(x=True, y=True)

        return p
        
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
        self.OpenPortButton.setEnabled(False)
        self.ClosePortButton.clicked.connect(self.close_port) #关闭串口1
        self.ClosePortButton.setEnabled(False)
        self.OpenPortButton_2.clicked.connect(self.open_port_2) #打开串口2
        self.OpenPortButton_2.setEnabled(False)
        self.ClosePortButton_2.clicked.connect(self.close_port_2) #关闭串口2
        self.ClosePortButton_2.setEnabled(False)

        self.CleanOutPutButton.clicked.connect(self.clean_ack_windows) #清理窗口输出
        self.CleanOutPutButton_2.clicked.connect(self.clean_ack_windows_2)

        self.uart_port_work_thread = UartThread(self) #串口1收发工作线程
        self.uart_port_work_thread.trigger.connect(self.uart_ACK_display)
        self.uart_port_work_thread_2 = UartThread(self) #串口2收发工作线程
        self.uart_port_work_thread_2.trigger.connect(self.uart_ACK_display_2)

        self.uart_port_check_thread = UartPortCheckThread(self) #系统串口检查
        self.uart_port_check_thread.trigger.connect(self.uart_port_scan)
        self.uart_port_check_thread.start()

        self.CMDTypeBox.activated.connect(self.select_cmd_type) # 指令类型选择

        self.MsgTypeBox.activated.connect(self.select_msg_type) # 信息类型选择
        self.SensorTypeBox.activated.connect(self.select_sensor_type)# 传感器类型选择
        self.SensorNumBox.activated.connect(self.select_sensor_num)# 传感器编号选择
        self.SpaceNumBox.activated.connect(self.select_space_num)# 设备空间号选择
        r'''演示选项卡组件
        '''
        self.StartDemo.clicked.connect(self.start_demo)#开始演示
        self.StartDemo.setEnabled(False)
        self.EndDemo.clicked.connect(self.end_demo)#关闭演示
        self.EndDemo.setEnabled(False)
        self.timer = QTimer(self)#设置演示轮询定时器
        self.timer.timeout.connect(self.demo_cmd_poll) 
        self.SpaceBox.activated.connect(self.select_display_space)#选择激活页面

        self.graph_update_timer = QTimer(self)
        self.graph_update_timer.timeout.connect(self.demo_graph_poll)
        
        self.SpaceItemTree.clicked.connect(self.demo_select_sensor)

    def start_demo(self):
        self.uart_port_work_thread.trigger.connect(self.demo_data_struct) #串口1线程绑定显示窗口
        self.timer.start(5000) #轮询周期5s
        self.graph_update_timer.start(5000)
        self.timebase = int(time.time()) #设定时间戳基准

        self.StartDemo.setEnabled(False)
        self.EndDemo.setEnabled(True)

    def end_demo(self):
        self.timer.stop()
        self.graph_update_timer.stop()
        self.uart_port_work_thread.trigger.disconnect(self.demo_data_struct) #串口1线程解绑显示窗口
        self.timebase = 0 #时间戳基准归零

        if self.ClosePortButton.isEnabled():
            self.StartDemo.setEnabled(True)
        self.EndDemo.setEnabled(False)

    def demo_data_struct(self,value:dict):

        tree = self.demo_data_table
        contain = eval(value["ACK"].decode("ascii"))
        if contain["Type"] == "SENSOR":
            contain = contain["Content"]
            while len(contain["Device"])<4:
                contain["Device"] +='0'
            flag = update_data_tree(tree,contain)
            self.demo_data_table = tree

            keys = list(tree.keys())
            keys = [str(i) for i in keys]
            if keys != self.demo_space:       
                self.SpaceBox.clear()
                self.SpaceBox.addItems(keys)
                self.demo_display_space = self.SpaceBox.currentText()
                self.demo_space = keys
            #显示表和树形结构
            if flag == True:
                self.demo_tree_display(self.demo_data_table[eval(self.demo_display_space)])
            a=[contain]
            insert_data(a)
        

    def select_display_space(self):
        self.demo_display_space = self.SpaceBox.currentText()
        self.demo_tree_display(self.demo_data_table[eval(self.demo_display_space)])

    def demo_tree_display(self,table:dict):
        self.SpaceItemTree.clear()
        #设置根节点
        
        for typ in table:
            type_node=QTreeWidgetItem(self.SpaceItemTree)
            type_node.setText(0,f"传感类型{typ}")
            for dev in table[typ]:
                device_node=QTreeWidgetItem(type_node)
                device_node.setText(0,f"设备{str(dev)}")
                for sen in table[typ][dev]:
                    sensor_node=QTreeWidgetItem(device_node)
                    sensor_node.setText(0,f"传感器{sen}")

        self.SpaceItemTree.expandAll()


    def demo_cmd_poll(self):

        if self.OpenPortButton.isEnabled():
            self.DemoDataBrowser.setText("请打开串口1")
        else:
            timestamp = format(int(time.time()),'x')
            content = "01"+timestamp
            cmdstr ,_,_= cmd_pack(content)  #包装命令帧
            self.uart_port_work_thread.pipe.emit({"content":bytes.fromhex(cmdstr),"signal":True}) #同步时间戳
            time.sleep(0.1)
            content = "03"+"0001"
            cmdstr ,_,_= cmd_pack(content)  #包装命令帧
            self.uart_port_work_thread.pipe.emit({"content":bytes.fromhex(cmdstr),"signal":True}) #同步时间戳

    def demo_graph_poll(self):
       if self.now_select_sensor ==None:
           pass 
       else:
            xdata, ydata = read_data(self.now_select_sensor)
            
            if len(self.xdata_list)<self.list_num:
                self.xdata_list.append(float(ydata))
            else:
                self.xdata_list[:-1] = self.xdata_list[1:]
                self.xdata_list.append(float(ydata))
            
            self.graph.plot().setData(self.xdata_list)

    def demo_select_sensor(self):
        item=self.SpaceItemTree.currentItem()
        if item.text(0)[:3] == '传感器':
            self.xdata_list = []
            sensor = item.parent().text(0)[2:] + item.text(0)[3:]
            self.now_select_sensor = sensor


    def open_port(self):
        self.uart_port_work_thread.pipe.emit({"port":self.port})
        self.uart_port_work_thread.start() # 开启串口1工作线程

        self.SendCMDButton.setEnabled(True)
        self.ClosePortButton.setEnabled(True)
        self.OpenPortButton.setEnabled(False)
        if self.EndDemo.isEnabled():
            pass
        else:
            self.StartDemo.setEnabled(True)

    def close_port(self):
        self.uart_port_work_thread.pipe.emit({"signal":"close"})

        self.SendCMDButton.setEnabled(False)
        self.ClosePortButton.setEnabled(False)
        self.OpenPortButton.setEnabled(True)

    def open_port_2(self):
        self.uart_port_work_thread_2.pipe.emit({"port":self.port_2})
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

        cmdstr ,label,crc= cmd_pack(content)  #包装命令帧

        self.CRCDisplay.setText(crc) # 在UI中显示相关内容
        self.CMDLabelDisplay.setText(label)
        self.CMDBrowser.setText(cmdstr+"字节数:"+str(int(len(cmdstr)/2)))

        return cmdstr

    def send_cmd(self):
        r'''发送指令按钮回调函数
        '''
        cmd = bytes.fromhex(self.generate_cmd())#获取指令内容,转换为二进制
        self.uart_port_work_thread.pipe.emit({"content":cmd,"signal":True})
        if self.ACKcheck.isChecked(): #模拟mesh回复ACK
            ack,_ = msg_pack("03"+self.CMDLabelDisplay.toPlainText())
            time.sleep(0.1)
            self.uart_port_work_thread_2.pipe.emit({"content":bytes.fromhex(ack),"signal":True})
            

    def generate_msg(self)->str:

        sensor_data = self.SensorData.text()
        device_address = self.DeviceAddress.text()
        #根据信息类型选择内容
        if self.msg_type == "01":
            content = self.msg_type+device_address+self.space_num+self.sensor_num+self.sensor_type+sensor_data
        elif self.msg_type == "02":
            content = ''

        msgstr,crc=msg_pack(content)

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
        type_dict = mesh信息类型
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
        type_dict = 传感器类型
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
        type_dict = 指令类型

        self.cmd_type = type_dict[self.CMDTypeBox.currentText()]

    def select_port_type(self):
        r'''选择串口类型（windows/linux）
        '''
        self.port = self.SerialPortTypeBox.currentText()

    def select_port_type_2(self):
        r'''选择串口2类型（windows/linux）
        '''
        self.port_2 = self.SerialPortTypeBox_2.currentText()

    def uart_ACK_display(self,value:dict):
        r'''串口1信号回调函数
        '''
        global timec
        if type(value["ACK"]) == bytes:
            contain = value["ACK"].decode("ascii")
            self.ACKDisplay.append(contain+"字节数："+str(len(contain)))

            contain = eval(contain)
            self.ACKParserWindow.append(f"""响应类型：{contain["Type"]}
                                            响应内容：{contain["Content"]}
                                            响应时间：{value["Time"]-timec}s
                                        """)
        else:
            contain = str(value["ACK"])
            self.ACKDisplay.append(contain)


    def uart_ACK_display_2(self,value:dict):
        r'''串口2信号回调函数
        '''
        self.ACKDisplay_2.append(value["ACK"]+"字节数："+str(len(value["ACK"])))

    def uart_port_scan(self,ports:list):
        r'''串口扫描更新回调
        '''
        self.SerialPortTypeBox.clear()
        self.SerialPortTypeBox.addItems(ports)

        self.SerialPortTypeBox_2.clear()
        self.SerialPortTypeBox_2.addItems(ports)

        self.port = self.SerialPortTypeBox.currentText()
        self.port_2 = self.SerialPortTypeBox_2.currentText()

        if self.ClosePortButton.isEnabled() == False:
            self.OpenPortButton.setEnabled(True)
        if self.ClosePortButton_2.isEnabled() == False:
            self.OpenPortButton_2.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
