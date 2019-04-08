## ネット対戦野球盤
受信部分のコード。  
AWS SQS上のメッセージをPythonで受信し、Arduinoへシリアル通信を送る。  
* baseball.py : 受信するPythonスクリプト。
* baseball.ino : Arduino側のコード。

## 仮想環境の作成
```
$ virtualenv -p python3 baseball
$ pip install pyserial awscli boto3
```

## AWS認証情報の設定
```
$ aws configure
```
を実行して認証情報を入力する。  
See : https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-chap-configure.html
