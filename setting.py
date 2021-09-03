#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from prettytable import PrettyTable
import time

os.system("clear")
x = PrettyTable()
x.field_names = ["N", "Run"]
x.add_rows(
    [
        [1, "Uninstall OS"],
        [2, "Change login"],
        [3, "Change password"],
        [4, "Initialize recovery"],
        [5, "Add your script into recovery"],
        [6, "Restart chroot menu with root"],
        [7, "Reinstall OS"],
        [8, "Reinstall recovery"],
        [9, "Uninstall recovery"],
        [10, "Uninstall proot-distro system"],
        [11, "Uninstall atilo system"],
        [12, "Exit to chroot menu"],
    ]
)
print(x)
print("Select your function:")
a = int(input())

if a == 1:
    print("Are you seriously want uninstall OS? yes/no")
    b = input()

    if b == 'yes':
        os.system("bash /data/data/com.termux/files/system/uninstall.sh")
        os.system("bash")
    elif b == 'no':
        os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 2:
    os.system("python3 /data/data/com.termux/files/chroot/chlogin.py")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 3:
    os.system("python3 /data/data/com.termux/files/chroot/chpass.py")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 4:
    os.system("bash /data/data/com.termux/files/.initialize/initialize.sh")
    time.sleep(5)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 5:
    os.system("python3 /data/data/com.termux/files/.initialize/initialize.py")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 6:
    os.system("clear && sudo python3 /data/data/com.termux/files/chroot/chroot.py")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 7:
    print("Are you seriously want to reinstall OS? yes/no")
    c = input()

    if c == 'yes':
        os.system("bash /data/data/com.termux/files/system/uninstall.sh && rm -rf /data/data/com.termux/files/home/STALIN-OS-term-edition && cd /data/data/com.termux/files/home && git clone https://github.com/Dima-diep/STALIN-OS-term-edition &>/dev/null && cd STALIN-OS-term-edition && chmod 777 install.sh && bash install.sh && clear && python3 /data/data/com.termux/files/boot/grub.py")
    elif c == 'no':
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 8:
    os.system("rm -rf /data/data/com.termux/files/.recovery && bash /data/data/com.termux/files/.initialize/initialize.sh")
    time.sleep(5)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 9:
    os.system("rm -rf /data/data/com.termux/files/.recovery")
    print("Recovery has been uninstalled")
    time.sleep(5)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 10:
    os.system("clear")
    print("System for uninstall")
    d = input()
    os.system("proot-distro remove " + d)
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 11:
    os.system("clear")
    print("System for uninstall")
    e = input()
    os.system("python3 /data/data/com.termux/files/usr/bin/atilo remove " + e)
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py") 
elif a == 12:
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
