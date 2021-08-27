#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

print("Write pass by 'pass' (not pass)")
print("Old pass:")
a = input()
print("New pass:")
b = input()

with open("/data/data/com.termux/files/boot/pass.py", "r") as f:
    raw = f.read().lower().replace(a, b)
    file = open("/data/data/com.termux/files/boot/pass.py", "w")
    file.write(raw)
    file.close()
    f.close()
