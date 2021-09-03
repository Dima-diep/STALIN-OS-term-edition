#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from prettytable import PrettyTable

print("WARNING! YOU STARTED RECOVERY MODE! BE CAREFUL BECAUSE YOU CAN DESTROY SYSTEM!!!")
print(" ")
print(" ")
x = PrettyTable()
x.field_names = ["N", "Function", "Root need?"]
x.add_rows(
    [
        [1, "Shutdown mobile", "Yes"],
        [2, "bootloop mobile (it isn't destroy mobile bootfs,\n just calling bootloop", "Yes"],
        [3, "Run my bash script", "No"],
        [4, "Back to GRUB", "No"],
    ]
)
print(x)
print("Select:")
l = int(input())

if l == 1:
    os.system("bash /data/data/com.termux/files/.recovery/script1.sh || python3 /data/data/com.termux/files/boot/grub.py")
elif l == 2:
    os.system("bash /data/data/com.termux/files/.recovery/script2.sh || python3 /data/data/com.termux/files/boot/grub.py")
elif l == 3:
    os.system("ls /data/data/com.termux/files/.recovery")
    print("Run your bash script:")
    m = input()
    os.system("bash /data/data/com.termux/files/.recovery/" + m + " && clear && python3 /data/data/com.termux/files/boot/grub.py")
elif l == 4:
    os.system("clear && python3 /data/data/com.termux/files/boot/grub.py")
