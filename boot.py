#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time

os.system("clear")
print("Mounting chroot...")
time.sleep(0.5)
print("Mounting system...")
time.sleep(0.5)
print("Mounting bin...")
time.sleep(1)
print("Mounting home...")
time.sleep(1)
os.system("mpv /data/data/com.termux/files/boot/login.mp3 && clear && python3 /data/data/com.termux/files/chroot/chroot.py")
