#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from prettytable import PrettyTable

os.system("clear")
print("Terminal tools v3.1")
print("S - Root need only for some options")
x = PrettyTable()
x.field_names = ["N", "Tools", "Root"]
x.add_rows(
    [
        [1, "nmap", "S"],
        [2, "netcat", "S"],
        [3, "metasploit", "N"],
        [4, "apache", "N"],
        [5, "geomac", "N"],
        [6, "bettercap", "Y"],
        [7, "mitmproxy", "N"],
        [8, "evil-ssdp", " N"],
        [9, "WiFite", "Y"],
        [10, "exit", " "],
    ]
)
print(x)
print("Select your tool:")
a = int(input())

if a == 1:
    os.system("clear")
    print("Select options and port/domain: (ex. -Pn -A)")
    print("For some options, you need root!")
    b = input()
    print("Save results into txt? y/n")
    d = input()

    if d == 'y':
        print("Text result (full path)")
        e = input()
        os.system("nmap " + b + " >> " + e)
        os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
    elif d == 'n':
        os.system("nmap " + b)
        for g in range(0, 9999999999):
            print("Press e for exit")
            f = input()

            if f == 'e':
                break
            else:
                exit
        os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 2:
    os.system("clear")
    print("Select options and port: (ex. -lp 23)")
    print("For the listening port 1-1023, you need root permission")
    h = input()
    print("For exiting, press Ctrl-C (not Ctrl-Z!)")
    os.system("ncat " + h)
    os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 3:
    os.system("msfconsole")
    os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 4:
    print("Write option:")
    i = input()
    os.system("apachectl " + i)
    for j in range(0, 9999999999):
        print("Press e for exit")
        k = input()

        if k == 'e':
            break
        else:
            exit
    os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 5:
    print("Write your functions:")
    l = input()
    os.system("geomac " + l)
    for m in range(0, 9999999999):
        print("Press e for exit")
        n = input()

        if n == 'e':
            break
        else:
            exit
    os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 6:
    os.system("sudo bettercap")
    os.system("python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 7:
    print("Write your parameters (with \" \" in start) or run without it")
    o = input()
    os.system("mitmproxy" + o)
    os.system("python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 8:
    os.system("python3 /data/data/com.termux/files/home/evil-ssdp/evil-ssdp.py")
    os.system("python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 9:
    print("Write your parameters or run without it")
    p = input()
    os.system("sudo python3 /data/data/com.termux/files/home/Wifite/Wifite.py " + p)
    os.system("python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 10:
    x = PrettyTable()
    x.field_names = ["N", "Option"]
    x.add_rows(
        [
            [1, "Exit to chroot"],
            [2, "Exit to GRUB"],
        ]
    )
    print(x)
    q = int(input())

    if q == 1: 
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif q == 2:
        os.system("clear && python3 /data/data/com.termux/files/boot/grub.py")
