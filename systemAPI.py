import random
from ctypes import CDLL,c_uint,c_uint8


class Tools():

    mesh信息类型 = {   
                        "传感信息":"01",
                        "路由信息":"02",
                  }

    传感器类型 = {   
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
    指令类型 =  {   
                        "时间同步":"01",
                        "节点控制":"02",
                        "信息获取":"03",
               }
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

        #32bit无符号整数16进制形式
        if CRC < 0:
            CRC = 0x100000000+CRC
        CRC = format(CRC,'x')
        for i in range(8-len(CRC)):
            CRC = '0'+CRC

        return  CRC 

    def crc8_check(self,data:bytes)->str:
        r'''CRC8校验函数
        '''
        crc8 = CDLL("libcrc8.dll")
        datalen = len(data)
        DATASTR = c_uint8 * datalen
        datastr = DATASTR()
        for i in range(datalen):
            datastr[i] = int(data[i]) # 大端模式
        CRC = crc8.get_crc8(datastr,datalen)

        #8bit 无符号整数16进制形式
        if CRC < 0:
            CRC = 0x100 +CRC
        CRC = format(CRC,'x')
        if len(CRC)==1:
            CRC = '0'+CRC
        return CRC

    def msg_pack(self,content:str)->str:
        r'''模拟mesh信息打包函数，负责校验和帧包装
        '''
        seq = content.split()
        temp = ''
        content = temp.join(seq) #去除空白符

        SOH = "01"
        EOT = "04"
        ESC = "1B"

        crc = self.crc8_check(bytes.fromhex(content))
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