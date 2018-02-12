# AutoTSSSaver
Automatically detect the change of tss server and save blobs.

## How to use?
**1. Edit devices.ini**

First, you have to write device's information to devices.ini.

This is example:

```
[Soh's iPhone X]
identifier = iPhone10,3
ecid = D38913828002E
boardconfig = d22ap

[Soh's iPad Pro]
identifier = iPad7,3
ecid = E115E088B603A
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
(I just add some files to check tss saver automatically)
