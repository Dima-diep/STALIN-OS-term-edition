#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

try:
    print("Your login: ")
    a = input()

    login = 'oldlogin'

    if a == login:
        os.system("python3 /data/data/com.termux/files/boot/pass.py")
    elif a != login:
        os.system("python3 /data/data/com.termux/files/boot/login.py")
except KeyboardInterrupt:
    os.system("python3 /data/data/com.termux/files/boot/login.py")
