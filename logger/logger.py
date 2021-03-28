import gxsimcom
import memcache 
import re
import datetime
import time


def GetWordDeviceD(plc,db):
  for i in range(10):
    devicename = "D" + str(960*i)
    try:
      v = plc.BlockReadWord(devicename,960)
      mydict = GetDict(v,devicename)
      #print(devicename,mydict[devicename],v[0])
      db.set_multi(mydict,time=2)
    except KeyboardInterrupt:
      plc.close()
      print("CONNECTION CLOSE")

def GetDict(values,addr):
  index = int(re.sub(r'\D','',addr))
  device = re.sub(r'\d','',addr)
  i = 0
  mydict = {}
  for value in values:
    devicename = device + str(index + i)
    mydict[devicename] = value
    i = i + 1
  return mydict

if __name__ == '__main__':
  plc = gxsimcom.GXSim2Com()
  plc.Connect()
  db = memcache.Client(['localhost:11211'])

  try:
    base_time = time.time()
    next_time = 0
    interval = 1

    pretime = datetime.datetime.utcnow()

    while True:
      GetWordDeviceD(plc,db)

      now = datetime.datetime.utcnow()
      difftime = now - pretime
      pretime = now
      next_time = ((base_time - time.time()) % interval) or interval
      time.sleep(next_time)      
      print(datetime.datetime.utcnow(),difftime,"READ D0-D9599")
      
  except KeyboardInterrupt:
      plc.Close()
      print("CONNECTION CLOSE")
  #'''
