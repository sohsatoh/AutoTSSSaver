# AutoTSSSaver
Automatically detect the change of tss server and save blobs.

You can run it on Linux and Mac.

[Download Tsschecker for mac here](https://github.com/encounter/tsschecker/releases)

[日本語版の説明はこちら](https://github.com/sohsatoh/AutoTSSSaver/blob/master/README-JP.md)

## How to use

**0. Install Dependencies**

```
sudo apt-get install libssl-dev
sudo apt-get install python-pip
sudo pip3 install requests
sudo pip3 install dataset
sudo pip install mdfmonitor
```

↓If your machine is linux, you may also have to run this command.

```
mkdir .src
cd .src
git clone https://github.com/tihmstar/libirecovery && cd ./libirecovery && bash autogen.sh && sudo make install
git clone https://github.com/tihmstar/libcrippy && cd ./libcrippy && bash autogen.sh && sudo make install
git clone https://github.com/tihmstar/libfragmentzip && cd ./libfragmentzip && sudo bash autogen.sh && sudo make install
git clone https://github.com/tihmstar/libpartialzip && cd ./libpartialzip && sudo bash autogen.sh && sudo make install
git clone https://github.com/libimobiledevice/libplist.git && cd ./libpartialzip && sudo bash autogen.sh && sudo make install
```

**1. Edit devices.ini**

First, you have to write device's information to devices.ini.

This is example:

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


**2. Edit autorun.py**

At the end of autorun.py, there is such a line.

```
~
os.system('cd /home/pi/AutoTSSSaver;python3 autotss.py -p /home/pi/AutoTSSSaver/tsschecker_linux')
```

You have to provide a path to folder like this.

```
~
os.system('cd <PATH TO AUTOTSSSAVER>;python3 autotss.py -p <PATH TO TSSCHECKER>')
```

As testrun, please execute the command inside '' on Terminal.

**3. Run autorun.py**

Open terminal, and run autorun.py by python (not python3).


**4. (Optional) Run it by cron**
I highly recommend to run autorun.py by cron.

```
@reboot python <PATH TO AUTORUN.PY>
```


## Dependencies
- python
- python3
- requests
- dataset
- [tsschecker](https://github.com/encounter/tsschecker/releases)
- [mdfmonitor](https://github.com/alice1017/mdfmonitor)

## Thanks
[autotss](https://github.com/codsane/autotss) by codsane
(I just added some files to check tss saver automatically)

## Todo
- rewrite autorun.py for python3
(I know it is insane to use python and python3 at the same time lol)
