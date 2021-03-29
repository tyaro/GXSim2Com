# GXSimCom

## GxSim2 接続 ライブラリ
### ポイント
毎回 GXSim2 のポートが違うため、getGxSimPortNum()でGxSim2のプロセスIDを取得してポートを確認し、GXsim2にアクセスします。
※CPUのタイプによって QnUDSimRun2.exe か QnXSimRun2.exe が起動する模様

プロトコルが微妙にMCプロトコルと異なる・・・
※解析中

GXSim3はTCPでやりとりは行えないっぽい
とりあえずでやってみたのでソースは今後精査していきたいと思います。

## 使用方法
```py
pip install gxsimcom
```


GXWorks2 にて デバッグ⇒ シミュレーション開始してください
GXSim2走らせているPC上で実行して下さい。

## METHOD

### Connection
```py
    gxsim=GXSim2Com()
    gxsim.Connect()

     

    gxsim.Close()
```

### Read
BlockReadBit(startAddress,num) : ビットデバイス読込(開始アドレス,読込点数)
```py
    bitValues = gxsim.BlockReadBit("M0",64)
    print(bitValues)
```
BlockReadWord(startAddress,num) : ワードデバイス読込(開始アドレス,読込点数MAX960)
```py
    wordValues = gxsim.BlockReadWord("D0",960)
    print(wordValues)
```
BlockReadDword(startAddress,num):ダブルワードデバイス読込(開始アドレス,読込点数MAX480)
```py
    dwrodValues = gxsim.BlockReadDWord("D1030",480)
    print(dwrodValues)
```
BlockReadFloat(startAddress,num):単精度実数読込(開始アドレス,読込点数MAX480)
```py
    floatValues = gxsim.BlockReadFloat("D1030",480)
    print(floatValues)
```

### Write
WriteBit(Address,value):ビット書込(アドレス,値) ※書込後読返有
```py
    b = gxsim.WriteBit("M0",1)
    print(b)
```
WriteWord(Address,value):ワード書込(アドレス,値) ※書込後読返有
```py
    b = gxsim.WriteWord("D1030",100)
    print(b)
```
WriteDWord(Address,value):ダブルワード書込(アドレス,値) ※書込後読返有
```py
    b = gxsim.WriteDWord("D1030",999999)
    print(b)
```
WriteFloat(Address,value):単精度実数書込(アドレス,値) ※書込後読返有
読返しは有効桁6桁でしていますが、端数でFalseが返るときあるかも・・・
```py
    b = gxsim.WriteFloat("D1030",1.23)
    print(b)
```

## 使用 Library

[psutil](https://github.com/giampaolo/psutil) : BSD-3-Clause License


```
pip install psutil
```


