#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from termcolor import colored

os.system("clear")
print(colored("Terminal tools v2.1", 'yellow', 'on_grey'))
print(colored("|##############|", 'green', 'on_grey'))
print(colored("| 1.nmap       |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 2.netcat     |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 3.metasploit |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 4.apache     |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 5.geomac     |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 6.bettercap  |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 7.mitmproxy  |", 'green', 'on_grey'))
print(colored("|--------------|", 'green', 'on_grey'))
print(colored("| 8.exit       |", 'green', 'on_grey'))
print(colored("|##############|", 'green', 'on_grey'))
print(colored("Select your tool:", 'red', 'on_grey'))
a = int(input())

if a == 1:
    os.system("clear")
    print(colored("Select options and port/domain: (ex. -Pn -A)", 'yellow', 'on_grey'))
    print(colored("For some options, you need root!", 'red', 'on_grey'))
    b = input()
    print(colored("Save results into txt? y/n", 'cyan', 'on_grey'))
    d = input()

    if d == 'y':
        print(colored("Text result (full path)", 'magenta', 'on_grey'))
        e = input()
        os.system("nmap " + b + " >> " + e)
        os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
    elif d == 'n':
        os.system("nmap " + b)
        for g in range(0, 9999999999):
            print(colored("Press e for exit", 'yellow', 'on_grey'))
            f = input()

            if f == 'e':
                break
            else:
                exit
        os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 2:
    os.system("clear")
    print(colored("Select options and port: (ex. -lp 23)", 'yellow', 'on_grey'))
    print(colored("For the listening port 1-1023, you need root permission", 'red', 'on_grey'))
    h = input()
    print(colored("For exiting, press Ctrl-C (not Ctrl-Z!)", 'green', 'on_grey'))
    os.system("ncat " + h)
    os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 3:
    os.system("msfconsole")
    os.system("clear && python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 4:
    print(colored("Write option:", 'grey', 'on_white'))
    i = input()
    os.system("apachectl " + i)
    for j in range(0, 9999999999):
        print(colored("Press e for exit", 'green', 'on_grey'))
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
        print(colored("Press e for exit", 'green', 'on_grey'))
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
    print(colored("Write your parameters (with \" \" in start) or run without it", 'yellow', 'on_grey'))
    o = input()
    os.system("mitmproxy" + o)
    os.system("python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 8:
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
