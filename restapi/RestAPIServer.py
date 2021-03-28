from fastapi import FastAPI
app = FastAPI()

import gxsimcom
import json
from pydantic import BaseModel,Field
import struct 

plc = gxsimcom.GXSim2Com()
plc.Connect()

class ReadData(BaseModel):
  device: str = Field(...,title="先頭デバイス",example="D100")
  num: int = Field(...,title="読込数(1~960)",example=100)

class WriteBitData(BaseModel):
  device: str = Field(...,title="デバイス",example="X0")
  value: int = Field(...,title="書込値",example=1)

class WriteWordData(BaseModel):
  device: str = Field(...,title="デバイス",example="D100")
  value: int = Field(...,title="書込値",example=1)

class WriteFloatData(BaseModel):
  device: str = Field(...,title="デバイス種別",example="D200")
  value: float = Field(...,title="書込値",example=1.23)

@app.get("/")
def read_root():
  return "hogehoge"
  
@app.post("/BlockReadWord")
async def BlockReadWord(data:ReadData):
  reslut = plc.BlockReadWord(data.device,data.num)
  return json.dumps(reslut,ensure_ascii=False) 

@app.post("/BlockReadFloat")
async def BlockReadFloat(data:ReadData):
  reslut = plc.BlockReadFloat(data.device,data.num)
  return json.dumps(reslut,ensure_ascii=False) 

@app.post("/BlockReadBit")
async def BlockReadBit(data:ReadData):
  reslut = plc.BlockReadBit(data.device,data.num)
  return json.dumps(reslut,ensure_ascii=False) 
  
@app.post("/WriteBit")
async def WriteBit(data:WriteBitData):
  result = plc.WriteBit(data.device,data.value)
  return result  

@app.post("/WriteWord")
async def WriteWord(data:WriteWordData):
  result = plc.WriteWord(data.device,data.value)
  return result


@app.post("/WriteFloat")
async def WriteFloat(data:WriteFloatData):
  result = plc.WriteFloat(data.device,data.value)
  return result

