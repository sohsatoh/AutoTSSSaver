#!/usr/bin/python

import os
from mdfmonitor import URLModificationMonitor

files = os.listdir(".")

# create Watcher instance
monitor = URLModificationMonitor()

# append file to mdfmonitor instance
monitor.add_url("https://api.ipsw.me/v2.1/firmwares.json")

print "started..."

for mdf in monitor.monitor():

    print mdf.url.center(30, "=")
    print "Catch the Modification!!"
    print "Old timestamp: %s" % mdf.old_dtime
    print "New timestamp: %s" % mdf.new_dtime
    os.system('cd ~/backup/shsh/autotss;python3 autotss.py -p /home/pi/backup/shsh/autotss/tsschecker_linux')
