#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

print("Write login by 'login' (not login)")
print("Old login:")
a = input()
print("New login:")
b = input()

with open("/data/data/com.termux/files/boot/login.py", "r") as f:
    raw = f.read().lower().replace(a, b)
    file = open("/data/data/com.termux/files/boot/login.py", "w")
    file.write(raw)
    file.close()
    f.close()
