#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored
from prettytable import PrettyTable

os.system("bash /data/data/com.termux/files/system/.killhist.sh")
os.system("clear")
print("---------------------------------")
os.system("uname -a")
print(" ")
print("Termux GRUB v3.1 by Dima-diep")
print("STALIN-OS term-edition v2.8.1 by Dima-diep")
x = PrettyTable()
x.field_names = ["N", "Option"]
x.add_rows(
    [
        [1, "STALIN OS"],
        [2, "proot-system login"],
        [3, "proot-system installer"],
        [4, "OS-Recovery Mode"],
    ]
)
print(x)
print("For exit, press Ctrl-C or Ctrl-Z")
os.system("python3 /data/data/com.termux/files/boot/login.py")
print("Select your system: ")
a = int(input())

if a == 1:
    os.system("clear")
    os.system("python3 /data/data/com.termux/files/boot/boot.py")

elif a == 2:
    os.system("clear")
    time.sleep(2.5)
    x = PrettyTable()
    x.field_names = ["N", "Type of system"]
    x.add_rows(
        [
            [1, "atilo"],
            [2, "proot-distro"],
            [3, "Andronix OS"],
        ]
    )
    print(x)
    print("Your proot type: ")
    b = int(input())

    if b == 1:
        print("Your OS: ")
        c = input()
        print("Mounting " + c + " rootfs...")
        time.sleep(1)
        os.system("python3 /data/data/com.termux/files/usr/bin/atilo pull " + c)
        os.system("python3 /data/data/com.termux/files/boot/grub.py")
    elif b == 2:
        print("Your OS: ")
        d = input()
        print("Mounting " + d + " rootfs...")
        time.sleep(1)
        os.system("proot-distro login " + d)
        os.system("python3 /data/data/com.termux/files/boot/grub.py")
    elif b == 3:
        print("Your OS (filename without ./): ")
        e = input()
        print("Mounting " + e + " rootfs...")
        time.sleep(1)
        os.system("bash " + e)
        os.system("python3 /data/data/com.termux/files/boot/grub.py")
elif a == 3:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Type of installation"]
    x.add_rows(
        [
            [1, "atilo"],
            [2, "proot-distro Termux-repo"],
            [3, "Andronix OS"],
        ]
    )
    print(x)
    print("Select your type: ")
    f = int(input())

    if f == 1:
        print("List supported system:")
        os.system("python3 /data/data/com.termux/files/usr/bin/atilo images")
        print("What do you want install?")
        i = input()
        os.system("python3 /data/data/com.termux/files/usr/bin/atilo pull " + i)
        os.system("python3 /data/data/com.termux/files/usr/bin/atilo run " + i)
        os.system("python3 /data/data/com.termux/files/boot/grub.py")
    elif f == 2:
        os.system("clear && apt install proot proot-distro -yq && clear")
        os.system("proot-distro list")
        print("What system do you want install?")
        j = input()
        os.system("proot-distro install " + j)
        os.system("proot-distro login " + j)
        os.system("python3 /data/data/com.termux/files/boot/grub.py")

    elif f == 3:
        os.system("clear")
        os.system("cd /data/data/com.termux/files/home/Linux-Installer-Termux && chmod 777 *.py && chmod +x install-requirements.sh")
        os.system("bash install-requirements.sh")
        os.system("clear")
        print("The first installer can install Debian, Kali Linux, Ubuntu, Arch Linux, Manjaro, Fedora, Void, Alpine, BackBox, CentOS, openSUSE")
        print("---------------------------------------------")
        print("The second installer can install Debian, Kali Linux, Ubuntu, Manjaro, Parrot, Arch, Alpine, Fedora, Void")
        print("Select your system (1/2):")
        k = int(input())

        if k == 1:
            os.system("python3 linux.py")
            os.system("python3 /data/data/com.termux/files/boot/grub.py")
        elif k == 2:
            os.system("python3 linux2.py")
            os.system("python3 /data/data/com.termux/files/boot/grub.py")
elif a == 4:
    os.system("clear")
    print("WARNING! FOR ANY USAGE OF THIS MODE, YOU NEED INITIALIZE IT")
    time.sleep(1)
    if os.path.exists("/data/data/com.termux/files/.recovery"):
        os.system("python3 /data/data/com.termux/files/system/recovery.py")
    else:
        print("WARNING! THE RECOVERY MODE ISN'T INITIALIZED")
        time.sleep(2.5)
        os.system("clear && python3 /data/data/com.termux/files/boot/grub.py")
