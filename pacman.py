#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from prettytable import PrettyTable
from termcolor import colored

os.system("clear")
print("Hello! This is STALIN OS term-edition Package Manager!")
print("version 4.3 by Dima-diep")
print("WARNING! Package Manager isn't working with root")
x = PrettyTable()
x.field_names = ["N", "Name"]
x.add_rows(
    [
        [1, "Games"],
        [2, "Network Tools"],
        [3, "Compilers"],
        [4, "text editors"],
        [5, "SMS-Bombers"],
        [6, "Other Tools"],
        [7, "Install python2 library"],
        [8, "Install python3 library"],
        [9, "Install ruby library"],
        [10, "Install node-js (npm) library"],
        [11, "Help with command"],
        [12, "exit"],
    ]
)
print(x)
print("Select your type:")
a = int(input())

if a == 1:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Game"]
    x.add_rows(
        [
            [1, "0verkill"],
            [2, "angband"],
            [3, "bastet"],
            [4, "brogue"],
            [5, "cavez-of-phear"],
            [6, "cboard"],
            [7, "curse-of-war"],
            [8, "dmagnetic"],
            [9, "dopewars"],
            [10, "frotz"],
            [11, "glulxe"],
            [12, "gnuchess"],
            [13, "gnugo"],
            [14, "gnushogi"],
            [15, "gnuski"],
            [16, "greed"],
            [17, "lexter"],
            [18, "moon-buggy"],
            [19, "moria"],
            [20, "myman"],
            [21, "nethack"],
            [22, "ninvaders"],
            [23, "nsnake"],
            [24, "nudoku"],
            [25, "open-adventure"],
            [26, "pacman"],
            [27, "snake"],
            [28, "solitaire"],
            [29, "viletris"],
        ]
    )
    print(x)
    print("Select your game:")
    b = int(input())

    if b == 1:
        os.system("clear && apt install 0verkill -y")
    elif b == 2:
        os.system("clear && apt install angband -y")
    elif b == 3:
        os.system("clear && apt install bastet -y")
    elif b == 4:
        os.system("clear && apt install brogue -y")
    elif b == 5:
        os.system("clear && apt install cavez-of-phear -y")
    elif b == 6:
        os.system("clear && apt install cboard -y")
    elif b == 7:
        os.system("clear && apt install curse-of-war -y")
    elif b == 8:
        os.system("clear && apt install dmagnetic -y")
    elif b == 9:
        os.system("clear && apt install dopewars -y")
    elif b == 10:
        os.system("clear && apt install frotz -y")
    elif b == 11:
        os.system("clear && apt install glulxe -y")
    elif b == 12:
        os.system("clear && apt install gnuchess -y")
    elif b == 13:
        os.system("clear && apt install gnugo -y")
    elif b == 14:
        os.system("clear && apt install gnushogi -y")
    elif b == 15:
        os.system("clear && apt install gnuski -y")
    elif b == 16:
        os.system("clear && apt install greed -y")
    elif b == 17:
        os.system("clear && apt install lexter -y")
    elif b == 18:
        os.system("clear && apt install moon-buggy -y")
    elif b == 19:
        os.system("clear && apt install moria -y")
    elif b == 20:
        os.system("clear && apt install myman -y")
    elif b == 21:
        os.system("clear && apt install nethack -y")
    elif b == 22:
        os.system("clear && apt install ninvaders -y")
    elif b == 23:
        os.system("clear && apt install nsnake -y")
    elif b == 24:
        os.system("clear && apt install nudoku -y")
    elif b == 25:
        os.system("clear && apt install open-adventure -y")
    elif b == 26:
        os.system("clear && apt install pacman4console -y")
    elif b == 27:
        os.system("clear && apt install snake -y")
    elif b == 28:
        os.system("clear && apt install ttysolitaire -y")
    elif b == 29:
        os.system("clear && apt install viletris -y")
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")

elif a == 2:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Tools"]
    x.add_rows(
        [
            [1, "nmap+netcat"],
            [2, "metasploit"],
            [3, "apache"],
            [4, "sqlite3 (for reading databases)"],
            [5, "postgresql (need for metasploit)"],
            [6, "bettercap"],
            [7, "dirb"],
            [8, "aircrack-ng"],
            [9, "arp-scan"],
            [10, "mitmproxy"],
            [11, "evil-ssdp"],
            [12, "WiFite"],
        ]
    )
    print(x)
    print("Select your repo:")
    c = int(input())

    if c == 1:
        os.system("clear && apt install nmap nmap-ncat -y")
    elif c == 2:
        os.system("clear && cd /data/data/com.termux/files/home && git clone https://github.com/Dima-diep/Metasploit && cd Metasploit && chmod 777 * && bash metasploit.sh && cd -")
    elif c == 3:
        os.system("clear && cd /data/data/com.termux/files/home && git clone https://github.com/Dima-diep/apache-termux && cd apache-termux && chmod 777 * && bash apache.sh && cd -")
    elif c == 4:
        os.system("clear && apt install sqlite -y")
    elif c == 5:
        os.system("clear && apt install postgresql -y")
    elif c == 6:
        os.system("clear && apt install root-repo -y && apt install bettercap -y")
    elif c == 7:
        os.system("clear && apt install dirb -y")
    elif c == 8:
        os.system("clear && apt install root-repo -y && apt install aircrack-ng -y")
    elif c == 9:
        os.system("clear && apt install root-repo -y && apt install arp-scan -y")
    elif c == 10:
        os.system("clear && python3 -m pip install mitmproxy")
    elif c == 11:
        os.system("clear && git clone https://github.com/initstring/evil-ssdp")
    elif c == 12:
        os.system("clear && git clone https://github.com/derv82/wifite.git && apt install root-repo -y && apt install aircrack-ng -y")
    os.system("clear && python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 3:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Tools"]
    x.add_rows(
        [
            [1, "ruby2"],
            [2, "python 2.7"],
            [3, "rust"],
            [4, "swift"],
            [5, "c/c++"],
            [6, "golang"],
            [7, "php"],
            [8, "java"],
            [9, "javascript"],
            [10, "javascript-lts"],
            [11, "kotlin"],
            [12, "julia"],
        ]
    )
    print(x)
    print("Select your compiler:")
    d = int(input())

    if d == 1:
        os.system("clear && cd /data/data/com.termux/files/home && wget -q https://hax4us.github.io/TermuxBlack/termuxblack.key -O termuxblack.key && apt-key add termuxblack.key && apt update -y && apt install ruby2 -y")
    elif d == 2:
        os.system("clear && apt install python2 -y")
    elif d == 3:
        os.system("clear && apt install rust -y")
    elif d == 4:
        os.system("clear && apt install swift -y")
    elif d == 5:
        os.system("clear && apt install libllvm llvm -y")
    elif d == 6:
        os.system("clear && apt install golang -y")
    elif d == 7:
        os.system("clear && apt install php php-apache -y")
    elif d == 8:
        os.system("clear && apt install openjdk-17 -y")
    elif d == 9:
        os.system("clear && apt install nodejs -y")
    elif d == 10:
        os.system("clear && apt install nodejs-lts -y")
    elif d == 11:
        os.system("clear && apt install kotlin -y")
    elif d == 12:
        os.system("clear && apt install julia -y")
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 4:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Editor"]
    x.add_rows(
        [
            [1, "nano"],
            [2, "vim"],
            [3, "neovim"],
            [4, "joe"],
            [5, "emacs"],
            [6, "micro"],
            [7, "mcedit"],
        ]
    )
    print(x)
    print("Select your editor:")
    e = int(input())

    if e == 1:
        os.system("clear && apt install nano -y")
    elif e == 2:
        os.system("clear && apt install vim -y")
    elif e == 3:
        os.system("clear && apt install neovim -y")
    elif e == 4:
        os.system("clear && apt install joe -y")
    elif e == 5:
        os.system("clear && apt install emacs -y")
    elif e == 6:
        os.system("clear && apt install micro -y")
    elif e == 7:
        os.system("clear && apt install mc -y")
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 5:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "SMS-Bombers"]
    x.add_rows(
        [
            [1, "T-Bomb"],
            [2, "SMSBomber300"],
            [3, "Egyptian-SMS-Spammer"],
            [4, "spymer"],
        ]
    )
    print(x)
    print("Select your bomber:")
    f = int(input())

    if f == 1:
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/TheSpeedX/TBomb && chmod 777 TBomb/*")
    elif f == 2:
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Ivan-Hacker-700/SMS-Bomber-300-Free && chmod 777 SMS-Bomber-300-Free/*")
    elif f == 3:
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/KendoClaw1/Egyptian-SMS-Spammer && chmod 777 Egyptian-SMS-Spammer/*")
    elif f == 4:
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/FSystem88/spymer && chmod 777 spymer/*")
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")

elif a == 6:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Tools"]
    x.add_rows(
        [
            [1, "Telegram Number Check"],
            [2, "system upgrade"],
            [3, "Install your package"],
            [4, "Clone your repository"],
            [5, "Create your package"],
            [6, "Remove your packages"],
            [7, "List Packages"],
        ]
    )
    print(x)
    print("Select your function:")
    g = int(input())

    if g == 1:
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Dima-diep/Telegram-numcheck && chmod 777 Telegram-numcheck/*")
    elif g == 2:
        os.system("clear && apt update -y && apt upgrade -y && python3 -m pip install --upgrade pip && clear")
    elif g == 3:
        print("Write list:" )
        h = input()
        os.system("clear && apt install " + h + " -y")
    elif g == 4:
        print("1.Git by link")
        print("2.Git by author/repo")
        print("3.Write command for cloning")
        bb = int(input())

        if bb == 1:
            print("Get your link:")
            j = input()
            os.system("cd /data/data/com.termux/files/home && git clone " + j)
            os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
        elif bb == 2:
            print("Get author/repo:")
            k = input()
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/" + k)
            os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
        elif bb == 3:
            print("Get your command without 'git clone':")
            l = input()
            os.system("cd /data/data/com.termux/files/home && git clone " + l)
            os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
    elif g == 5:
        print("Directory with files for your package (full path):")
        m = input()
        os.system("cd " + m + " && cp /data/data/com.termux/files/system/Manifest.json " + m)
        print("Program filename:")
        n = input()
        os.system("touch " + n)
        print("Run your favourite editor, then edit Manifest.json")
        o = input()
        os.system(o + " " + n + " && " + o + " Manifest.json && termux-create-package Manifest.json")
        print("Install this package? y/n")
        p = input()

        if p == 'y':
            os.system("dpkg -i *.deb")
        elif p == 'n':
            exit
    elif g == 6:
        print("Write list your packages:")
        r = input()
        os.system("clear && apt remove " + r + " -y && apt autoremove -y")
    elif g == 7:
        os.system("apt list > /data/data/com.termux/files/home/apt.list")
        print(colored("Check your list at File Manager, /data/data/com.termux/files/home/apt.list", 'cyan', 'on_grey'))
        time.sleep(5)
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 7:
    print(colored("Write your libraries or \"-r 'path-to-requirements.txt'\"", 'green', 'on_grey'))
    s = input()
    os.system("python2 -m pip install " + s)
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 8:
    print(colored("Write your libraries or \"-r 'path-to-requirements.txt'\"", 'green', 'on_grey'))
    t = input()
    os.system("python3 -m pip install " + t)
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 9:
    print(colored("Write your packages", 'green', 'on_grey'))
    u = input()
    os.system("gem install " + u)
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 10:
    print(colored("Write your packages", 'green', 'on_grey'))
    v = input()
    os.system("npm install " + v)
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 11:
    print(colored("Write command", 'green', 'on_grey'))
    w = input()
    os.system("man " + w)
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 12:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Select"]
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
