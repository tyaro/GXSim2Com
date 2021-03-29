import time
from concurrent import futures
import grpc
import melsec_pb2
import melsec_pb2_grpc
import gxsimcom
import json
import struct 

plc = gxsimcom.GXSim2Com()
plc.Connect()


class MelsecComServiceServicer(melsec_pb2_grpc.MelsecComServiceServicer):

    def __init__(self):
        pass
 
    def HelloMsg(self, request_iterator, context):
      for new_msg in request_iterator:
        reply_msgs = []
        print('Recive Message : {}'.format(new_msg.msg))
        reply_msgs.append(melsec_pb2.ReplyHello(reply_msg="Hi"))
        for message in reply_msgs:
          yield message

    def BlockReadFloat(self, request_iterator, context):
      for new_msg in request_iterator:
          reply_msgs = []
          s = 'Receive Read Float Device Command! [device: {},num: {}]'.format(new_msg.device, new_msg.num)
          print(s)
          d = plc.BlockReadFloat(new_msg.device,new_msg.num)
          reply_msgs.append(melsec_pb2.ReplyRead(reply_msg=str(d)))
          for message in reply_msgs:
              yield message

    def BlockReadWord(self, request_iterator, context):
      for new_msg in request_iterator:
          reply_msgs = []
          s = 'Receive Read Word Device Command! [device: {},num: {}]'.format(new_msg.device,new_msg.num)
          print(s)
          d = plc.BlockReadWord(new_msg.device,new_msg.num)
          reply_msgs.append(melsec_pb2.ReplyRead(reply_msg=str(d)))
          for message in reply_msgs:
              yield message

    def BlockReadBit(self, request_iterator, context):
      for new_msg in request_iterator:
          reply_msgs = []
          s = 'Receive Read Device Command! [device: {},num: {}]'.format(new_msg.device, new_msg.num)
          print(s)
          d = plc.BlockReadBit(new_msg.device,new_msg.num)
          reply_msgs.append(melsec_pb2.ReplyRead(reply_msg=str(d)))
          for message in reply_msgs:
              yield message

    def BlockWriteFloat(self, request_iterator, context):
      for new_msg in request_iterator:
          reply_msgs = []
          s = 'Receive Write Device Command! [device: {},value: {}]'.format(new_msg.device, new_msg.value)
          print(s)
          d = plc.WriteFloat(new_msg.device,new_msg.value)
          reply_msgs.append(melsec_pb2.ReplyWrite(reply_msg=d))
          for message in reply_msgs:
              yield message

    def BlockWriteBit(self, request_iterator, context):
      for new_msg in request_iterator:
          reply_msgs = []
          s = 'Receive Write Device Command! [device: {},value: {}]'.format(new_msg.device, new_msg.value)
          print(s)
          d = plc.WriteBit(new_msg.device,new_msg.value)
          reply_msgs.append(melsec_pb2.ReplyWrite(reply_msg=d))
          for message in reply_msgs:
              yield message

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    melsec_pb2_grpc.add_MelsecComServiceServicer_to_server(MelsecComServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC MelsecCom server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()                