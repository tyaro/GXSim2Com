import time
import threading
import json
import grpc
import melsec_pb2
import melsec_pb2_grpc
import ast
import datetime


def ReadFloatData(stub,Device,Num):
    messages = []
    messages.append(melsec_pb2.ReadMsg(device=Device,num=Num))
    responses = stub.BlockReadFloat(iter(messages))
    for response in responses:
        d = ast.literal_eval(response.reply_msg)
    return d

def ReadWordData(stub,Device,Num):
    messages = []
    messages.append(melsec_pb2.ReadMsg(device=Device,num=Num))
    responses = stub.BlockReadWord(iter(messages))
    for response in responses:
        d = ast.literal_eval(response.reply_msg)
    return d

def GetRunningStatus(d):
    for k,v in d.items():
        d[k] = int((v & 4) >> 2)
    return d

def HelloGrpc(stub):
    messages = []
    messages.append(melsec_pb2.HelloMessage(msg="Hello"))
    responses = stub.HelloMsg(iter(messages))
    for response in responses:
        d = response.reply_msg
    return d

'''
def worker():
    d = ReadFloatData(stub, "D1000",100)
    db.writeFloatData(client,d,"ProcessValue")
    time.sleep(0.1)
    d = ReadFloatData(stub, "D3900",8)
    db.writeFloatData(client,d,"ManipulatedValue")
    time.sleep(0.1)
    d = ReadWordData(stub,"D100",100)
    d = GetRunningStatus(d)
    db.writeBoolData(client,d)
    print(datetime.datetime.utcnow())
 

def schedule(interval, f):
    base_time = time.time()
    next_time = 0
    try:
        while True:
            t = threading.Thread(target=f)
            t.start()
            next_time = ((base_time - time.time()) % interval) or interval
            time.sleep(next_time)
    except KeyboardInterrupt:
            client.close()
            print("CONNECTION CLOSE")
'''
if __name__ == "__main__":
    #client = db.createInfluxdbClient()
    channel = grpc.insecure_channel('host.docker.internal:50051')
    stub = melsec_pb2_grpc.MelsecComServiceStub(channel)
    s = HelloGrpc(stub)
    print(s)
    d = ReadFloatData(stub,"D1000",100)
    print(d)




