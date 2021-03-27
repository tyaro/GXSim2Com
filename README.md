# GXSimCom

## GxSim2と通信を行うテスト

D1000から32ビット浮動小数点で250点読み出します。

毎回 GXSim2 のポートが違うため、getGxSimPortNum()でGxSim2のプロセスIDを取得してポートを確認し、GXsim2にアクセスします。

※CPUのタイプによって QnUDSimRun2.exe か QnXSimRun2.exe が起動する模様

プロトコルが微妙にMCプロトコルと異なる・・・
※解析中

GXSim3はTCPでやりとりは行えないっぽい

とりあえずでやってみたのでソースは今後精査していきたいと思います。

## 使用方法
- GXWorks2 でデバッグ⇒ シミュレーション開始
- `python gxsimcom.py` で起動
- コンソールにJson形式で読込結果を吐き出し




## 使用 Library

[psutil](https://github.com/giampaolo/psutil) : BSD-3-Clause License
[struct]
[binascii]
[socket]
[time]

```
pip install psutil
```


