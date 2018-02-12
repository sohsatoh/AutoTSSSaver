# AutoTSSSaver
SHSH2の発行状態を自動的にチェックし、変更が検知された際に保存するスクリプトです。

## 使い方

**0. 依存パッケージのインストール**

```
sudo apt-get install libssl-dev
sudo apt-get install python-pip
sudo pip3 install requests
sudo pip3 install dataset
sudo pip install mdfmonitor
```

(python3やpip3のインストールを済ませておいてください。）

**1. devices.iniの編集**

devices.iniにデバイス情報を記載します。

以下例

```
[Soh's iPhone X]
identifier = iPhone10,6
ecid = D389138280023
boardconfig = d22ap

[Soh's iPad Pro]
identifier = iPad7,6
ecid = E115E088B6000
boardconfig = j207ap
```


**2. autorun.pyの編集**

autorun.pyの最下部に以下のような行があります。

```
~
os.system('cd /home/pi/AutoTSSSaver;python3 autotss.py -p /home/pi/AutoTSSSaver/tsschecker_linux')
```

ファイルを編集し、AutoTSSSaverへのパスを記載してください。

```
~
os.system('cd <AutoTSSSaverフォルダへのパス>;python3 autotss.py -p <tsscheckerへのパス>')
```

**3. autorun.pyの実行**

python3ではなく、pythonでautorun.pyを実行してください。


**4. (オプション) cronで再起動時に自動実行**
cronを使用し、再起動後に自動でスクリプトを常駐させます。
こちらはオプションですが、最も重要な設定でもあります。
crontab -eで編集画面に入り、

```
@reboot python <PATH TO AUTORUN.PY>
```

を記載してください。


## 依存パッケージ
- python
- python3
- requests
- dataset
- [tsschecker](https://github.com/encounter/tsschecker/releases)
- [mdfmonitor](https://github.com/alice1017/mdfmonitor)

## Thanks
[autotss](https://github.com/codsane/autotss) by codsane
(I just add some files to check tss saver automatically)

## やること
- autorun.pyをpython3用に書き換え
（現段階では必要なファイルを集めただけで、ほぼ私が書いたスクリプトはありません）
