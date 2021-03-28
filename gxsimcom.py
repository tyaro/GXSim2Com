import util
import struct
import binascii
import gxsimdef
import socket
import re

def hex2float(s):
    if s.startswith('0x'):
        s = s[2:]
    s = s.replace(' ', '')
    return struct.unpack('<f', binascii.unhexlify(s))[0]

def hex2word(s):
    if s.startswith('0x'):
        s = s[2:]
    s = s.replace(' ', '')
    return struct.unpack('<h', binascii.unhexlify(s))[0]


class GXSim2Com():
    targetIp = "127.0.0.1"
    targetPort = 0
    bufferSize = 2048
    tcpClient = None

    send_header = [
        0x01,0x00,
    ]
    send_Datalen1 = [
        0x00,0x00,
    ] 
    send_const1 = [
        0xFD,0x00,  #
        0xFF,0xFF,  #
        0x00,0x00,  #
        0x11,0x11,  #
        0xFF,0x00,  #自局PC番号？
        0x00,0xFF,  #
        0xFF,0x03,  #自局CPU?
        0x00,0x00,  #
        0xFF,0x03,  #自局CPU?
        0x00,0x00,  #
    ]
    send_Datalen2 = [
        0x00,0x00,
    ]
    send_const2 = [
        0x1C,0x08,  #
        0x0A,0x08,  #
        0x00,0x00,  #
        0x00,0x00,  #
        0x00,0x00,  #
    ]

    cmd_blockread = [
        0x00,0x00,  #
        0x04,0x01,  #一括読込コマンド
        0x00,0x00,  #
        0x00,0x00,  #サブコマンド？
    ]



    def __init__(self):
        pass

    def Connect(self):
        self.targetPort = util.getGXSimPortNum()
        self.tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpClient.connect((self.targetIp,self.targetPort))
        print("CONNECTION OPEN")

    def Close(self):
        self.tcpClient.close()

    def _send(self,data):
        self.tcpClient.send(data)
    
    def _receive(self,dataSize):
        data = bytes()
        '''
        data += self.tcpClient.recv(self.bufferSize)
        print(len(data))
        print(dataSize)        
        '''
        if len(data) < dataSize:
            while True:
                data += self.tcpClient.recv(self.bufferSize)
                if len(data) == dataSize:
                    break
                elif len(data) > dataSize:
                    data = None
                    break
        #'''
        return data


    def BlockReadBit(self,startAddress,num):
        code,addr = self.getDeviceCode(startAddress)
        hnum = struct.pack("<H",num)
        if code == "0x00":
            return None
        data = bytes(self.send_const2)
        data += bytes(self.cmd_blockread)
        data += bytes(code)
        data += bytes(addr)
        data += bytes(hnum)

        sendData = self.conbineSenddata(data)
        self._send(sendData)
        size = -(-num // 16)*2 + 46
        r = self._receive(size)
        values = []
        for index in range(46,len(r),2):
            w = '{:02x}'.format(r[index+0]) + '{:02x}'.format(r[index+1])
            b = '{:016b}'.format(hex2word(w))
            for value in b:
                values.append(int(value))
        return values

    def BlockReadWord(self,startAddress,num):
        if num > 960:
            num = 960
            
        code,addr = self.getDeviceCode(startAddress)
        hnum = struct.pack("<H",num)
        if code == "0x00":
            return None

        data = bytes(self.send_const2)
        data += bytes(self.cmd_blockread)
        data += bytes(code)
        data += bytes(addr)
        data += bytes(hnum)

        sendData = self.conbineSenddata(data)
        self._send(sendData)
        size = num * 2 + 46
        r = self._receive(size)
        values = []
        for index in range(46,len(r),2):
            s = '{:02x}'.format(r[index+0]) + '{:02x}'.format(r[index+1])
            values.append(hex2word(s))
        return values

        #print(''.join([r'\x{:02x}'.format(x) for x in r] ))

    def BlockReadFloat(self,startAddress,num):
        if num > 480:
            num = 480
            
        code,addr = self.getDeviceCode(startAddress)
        hnum = struct.pack("<H",num*2)
        if code == "0x00":
            return None

        data = bytes(self.send_const2)
        data += bytes(self.cmd_blockread)
        data += bytes(code)
        data += bytes(addr)
        data += bytes(hnum)

        sendData = self.conbineSenddata(data)
        self._send(sendData)
        size = num * 4 + 46
        r = self._receive(size)
        values = []
        for index in range(46,len(r),4):
            s = '{:02x}'.format(r[index+0]) + '{:02x}'.format(r[index+1]) + '{:02x}'.format(r[index+2]) + '{:02x}'.format(r[index+3]) 
            values.append(hex2float(s))
        return values


    def conbineSenddata(self,requestdata):
        data = requestdata
        self.send_Datalen2 = struct.pack("<H",len(data))
        data = bytes(self.send_Datalen2) + data
        data = bytes(self.send_const1) + data
        self.send_Datalen1 = struct.pack("<H",len(data))
        data = bytes(self.send_Datalen1) + data
        data = bytes(self.send_header) + data

        return data


    def getDeviceCode(self,addr):
        for pattern in gxsimdef.deviceType:
            result = re.match(pattern,addr)
            if result:
                break
        code = [gxsimdef.deviceType[pattern]["code"] , 0]
        base = gxsimdef.deviceType[pattern]["base"]
        rowaddr = re.sub(pattern,'',addr)
        if base == 10:
            hexAddr = struct.pack("<L",int(rowaddr))
        else:
            hexAddr = struct.pack("<L",int("0x"+rowaddr,16))
        return code,hexAddr

  
if __name__ == "__main__":
    gxsim = GXSim2Com()
    gxsim.Connect()
    #gxsim.tcpClient.send(bytes(data))
    #r = gxsim.tcpClient.recv(2048)
    #mydict = readResponce(r,1000)
    #print(mydict)
    addr = "D0"
    wordValues = gxsim.BlockReadWord(addr,960)
    print(wordValues)
    bitValues =gxsim.BlockReadBit("M0",64)
    print(bitValues)
    bitValues =gxsim.BlockReadFloat("D1000",480)
    print(bitValues)
    gxsim.Close()

