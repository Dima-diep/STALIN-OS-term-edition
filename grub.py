#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

os.system("bash /data/data/com.termux/files/system/.killhist.sh")
os.system("clear")
print("---------------------------------")
os.system("uname -a")
print(" ")
print("Termux GRUB v2.1 by Dima-diep")
print("STALIN-OS term-edition v2.8.1 by Dima-diep")
print("|=== === === === === === === ===|")
print("| 1.STALIN OS                   |")
print("| 2.proot-system login          |")
print("| 3.proot-system installer      |")
print("| 4.OS-Recovery Mode            |")
print("|=== === === === === === === ===|")
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
    print("(===    ===   ===)")
    print("( 1.atilo        )")
    print("( 2.proot-distro )")
    print("( 3.Andronix OS  )")
    print("(===   ===    ===)")
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
    print(colored("|=== === === === === === === ===", 'grey', 'on_blue'))
    print(colored("| Types of installation:       |", 'grey', 'on_blue'))
    print(colored("|=== === === === === === === ===", 'grey', 'on_blue'))
    print(colored("| 1.atilo                      |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("| 2.proot-distro Termux-repo   |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("| 3.Andronix OS                |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("Select your type: ", 'grey', 'on_white'))
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
        print(colored("The first installer can install Debian, Kali Linux, Ubuntu, Arch Linux, Manjaro, Fedora, Void, Alpine, BackBox, CentOS, openSUSE", 'grey', 'on_blue'))
        print(colored("---------------------------------------------", 'grey', 'on_blue'))
        print(colored("The second installer can install Debian, Kali Linux, Ubuntu, Manjaro, Parrot, Arch, Alpine, Fedora, Void", 'grey', 'on_blue'))
        print(colored("Select your system (1/2):", 'grey', 'on_white'))
        k = int(input())

        if k == 1:
            os.system("python3 linux.py")
            os.system("python3 /data/data/com.termux/files/boot/grub.py")
        elif k == 2:
            os.system("python3 linux2.py")
            os.system("python3 /data/data/com.termux/files/boot/grub.py")
elif a == 4:
    os.system("clear")
    print(colored("WARNING! FOR ANY USAGE OF THIS MODE, YOU NEED INITIALIZE IT", 'yellow', 'on_grey'))
    time.sleep(1)
    if os.path.exists("/data/data/com.termux/files/.recovery"):
        os.system("python3 /data/data/com.termux/files/system/recovery.py")
    else:
        print(colored("WARNING! THE RECOVERY MODE ISN'T INITIALIZED", 'yellow', 'on_grey'))
        time.sleep(2.5)
        os.system("clear && python3 /data/data/com.termux/files/boot/grub.py")
