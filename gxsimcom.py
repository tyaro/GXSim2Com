import util
import struct
import binascii
import gxsimdef
import socket

data = gxsimdef.ReadDeviceBlock
deviceType = gxsimdef.deviceType

dev = "D"
data[44]=deviceType[dev]
print(data[44])
head = 1000


def hex_to_float(s):
    if s.startswith('0x'):
        s = s[2:]
    s = s.replace(' ', '')
    return struct.unpack('>f', binascii.unhexlify(s))[0]

def printData(dicData):
    for key in dicData.keys():
        s = key + ':' + "{:.2f}".format(dicData[key])

def readResponce(responce,headaddr):
    data = {}
    d = headaddr
    for index in range(46,len(responce),4):
        s = '{:02x}'.format(responce[index+3]) + '{:02x}'.format(responce[index+2]) + '{:02x}'.format(responce[index+1]) + '{:02x}'.format(responce[index+0])
        key = 'D{:04d}:f'.format(d)
        fdata = hex_to_float(s)
        data.setdefault(key,fdata)
        d = d + 2
    return data

#GX Simulator2に接続
targetIp = "127.0.0.1"
targetPort = util.getGXSimPortNum()
bufferSize = 2048 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((targetIp,targetPort))
print("CONNECTION OPEN")
tcp_client.send(bytes(data))
r = tcp_client.recv(bufferSize)
mydict = readResponce(r,1000)
print(mydict)
tcp_client.close()

