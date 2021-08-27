#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from termcolor import colored
import time

os.system("clear")
print(colored("| === === === === === === === ===  |", 'grey', 'on_white'))
print(colored("| 1.Uninstall OS                   |", 'grey', 'on_white'))
print(colored("| 2.Change login                   |", 'grey', 'on_white'))
print(colored("| 3.Change password                |", 'grey', 'on_white'))
print(colored("| 4.Initialize recovery            |", 'grey', 'on_white'))
print(colored("| 5.Add your script into recovery  |", 'grey', 'on_white'))
print(colored("| 6.Restart chroot menu with root  |", 'grey', 'on_white'))
print(colored("| 7.Reinstall OS                   |", 'grey', 'on_white'))
print(colored("| 8.Reinstall recovery             |", 'grey', 'on_white'))
print(colored("| 9.Uninstall recovery             |", 'grey', 'on_white'))
print(colored("| 10.Uninstall proot-distro system |", 'grey', 'on_white'))
print(colored("| 11.Uninstall atilo system        |", 'grey', 'on_white'))
print(colored("| 12.Exit to chroot menu           |", 'grey', 'on_white'))
print(colored("| === === === === === === === ===  |", 'grey', 'on_white'))
print(colored("Select your function:", 'grey', 'on_magenta'))
a = int(input())

if a == 1:
    print(colored("Are you seriously want uninstall OS? yes/no", 'yellow', 'on_grey'))
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
    print(colored("Are you seriously want to reinstall OS? yes/no", 'yellow', 'on_grey'))
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
    print(colored("Recovery has been uninstalled", 'yellow', 'on_grey'))
    time.sleep(5)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 10:
    os.system("clear")
    print(colored("System for uninstall", 'magenta', 'on_grey'))
    d = input()
    os.system("proot-distro remove " + d)
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 11:
    os.system("clear")
    print(colored("System for uninstall", 'magenta', 'on_grey'))
    e = input()
    os.system("python3 /data/data/com.termux/files/usr/bin/atilo remove " + e)
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py") 
elif a == 12:
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
