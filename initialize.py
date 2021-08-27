#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from termcolor import colored
import time

if os.file.exists("/data/data/com.termux/files/.recovery"):
    print("What script do you want load to recovery? Write full path")
    print("If your script isn't bash, then make bash script for starting it!")
    a = input()
    os.system("chmod 777 " + a)
    os.system("mv " + a + " /data/data/com.termux/files/.recovery")
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
else:
    print(colored("WARNING! RECOVERY MODE ISN'T INITIALIZED!", 'yellow', 'on_grey'))
    time.sleep(2.5)
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
        
