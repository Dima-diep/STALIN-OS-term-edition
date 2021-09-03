#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Chroot Menu"]
x.add_rows(
    [
        ["Contacts"],
        ["Music"],
        ["Package Manager"],
        ["Games"],
        ["Taskmgr Linux (Taskmgr)"],
        ["Telegram (supported for arm64)"],
        ["File Manager"],
        ["Terminal tools"],
        ["System menu"],
        ["Help for STALIN-OS"],
        ["Plugin Vim Install (PVI)"],
        ["Tor"],
        ["For developers"],
        ["Open file in android app (Open)"],
        ["Calculator"],
        ["Test Network Speed (TNS)"],
        ["Open fule into text editor (OFTE)"],
        ["Run SSH"],
        ["Exit to GRUB"],
    ]
)
print(x)
print("Run app:")
a = input()

if a == 'Contacts':
    os.system("clear && cat /data/data/com.termux/files/chroot/contacts.txt")
    print("---------------------------")
    print("It isn't working at root")
    print("1.Call")
    print("2.Add contact (add)")
    print("3.Exit")
    b = int(input())

    if b == 1:
        print("Contact for call:")
        c = input()
        os.system(c)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif b == 2:
        print("His name?")
        d = input()
        print("His phone (start +7...)")
        e = input()
        os.system("echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.bashrc && source ~/.bashrc")
        os.system("echo \"" + d + e + "\" >> ~/../chroot/contacts.txt")
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif b == 3:
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")

elif a == 'Music':
    os.system("clear && python3 /data/data/com.termux/files/home/Music-Termux/player.py")
    os.system("clear && python3 /data/data.com.termux/files/chroot/chroot.py")
elif a == 'Package Manager':
    os.system("python3 /data/data/com.termux/files/chroot/pacman.py")
elif a == 'Games':
    os.system("clear")
    print("Game for play:")
    h = input()
    os.system(h)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Taskmgr':
    os.system("htop")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Telegram':
    print("Do you want install Telegram (supported only for arm64) (y for install, n for login now")
    i = input()

    if i == 'y':
        os.system("apt install telegram-cli -yq")
        os.system("telegram-cli")
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif i == 'n':
        os.system("telegram-cli")
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'File Manager':
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "File Manager"]
    x.add_rows(
        [
            [1, "Check files"],
            [2, "Check all info for files"],
            [3, "Check attributes of files"],
            [4, "Find file in directory"],
            [5, "Execute file"],
            [6, "Make directory"],
            [7, "Make file"],
            [8, "Remove file/directory"],
            [9, "Totally remove file/directory"],
            [10, "Move/rename file/directory"],
            [11, "Copy file"],
            [12, "Copy directory"],
            [13, "Run file checker"],
            [14, "chmod/chattr"],
            [15, "Exit to chroot"],
        ]
    )
    print(x)
    print("Select your function")
    m = int(input())
    
    if m == 1:
        print("Directory:")
        ae = input()
        os.system("ls -a " + ae)
    elif m == 2:
        print("Directory:")
        af = input()
        os.system("ls -al " + af)
    elif m == 3:
        print("Directory:")
        ag = input()
        os.system("lsattr " + ag)
    elif m == 4:
        print("File name for find:")
        n = input()
        print("Directory where find:")
        o = input()
        os.system("ls -a " + o + " | grep " + n)
    elif m == 5:
        os.system("clear")
        x = PrettyTable()
        x.field_names = ["N", "Option"]
        x.add_rows(
            [
                [1, "Run bash script"],
                [2, "Run python2 script"],
                [3, "Run python3 script"],
                [4, "Run ruby script"],
                [5, "Run makefile"],
                [6, "Run compiled C/C++/Rust script"],
                [7, "Run go-lang script"],
                [8, "Compile java program"],
                [9, "Run java program"],
                [10, "Run php program"],
                [11, "Run swift program"],
                [12, "Compile rust program"],
            ]
        )
        print(x)
        n = int(input())
        
        if n == 1:
            print("Write path to script and parameters")
            o = input()
            os.system("bash " + o)
        elif n == 2:
            print("Write path to script and parameters")
            p = input()
            os.system("python2 " + p)
        elif n == 3:
            print("Write path to script and parameters")
            q = input
            os.system("python3 " + q)
        elif n == 4:
            print("Write path to script and parameters")
            r = input()
            os.system("ruby " + r)
        elif n == 5:
            print("Write directory with script")
            s = input()
            os.system("cd " + s)
            print("Write parameters or scriptname (if test.cpp, then write \"test\")")
            t = input()
            os.system("make " + t)
        elif n == 6:
            print("Write script directory")
            u = input()
            os.system("cd " + u)
            print("Write script name")
            v = input()
            os.system("./" + v)
        elif n == 7:
            print("Write script (full path)")
            w = input()
            os.system("go run " + w)
        elif n == 8:
            print("Write script directory")
            x = input()
            os.system("cd " + x)
            print("Write script name (if namescript is test.java, write \"test\"")
            y = input()
            os.system("javac " + y)
        elif n == 9:
            print("Full path to script")
            z = input()
            os.system("java " + z)
        elif n == 10:
            print("Full path to script")
            aa = input()
            os.system("php " + aa)
        elif n == 11:
            print("Full path to script")
            ab = input()
            os.system("swift " + ab)
        elif n == 12:
            print("Write working directory")
            ac = input()
            os.system("cd " + ac)
            print("Script name:")
            ad = input()
            os.system("rustc " + ad)
        time.sleep(5)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif m == 6:
        print("Write full path to new directory")
        ak = input()
        os.system("mkdir " + ak)
    elif m == 7:
        print("Write full path to new file")
        al = input()
        os.system("touch " + al)
    elif m == 8:
        print("Write full path to file/directory")
        am = input()
        os.system("rm -rf " + am)
    elif m == 9:
        print("Write full path to file/directory")
        an = input()
        os.system("shred -n 10 " + an)
    elif m == 10:
        print("Write full old path to file/directory")
        ao = input()
        print("Full path with new name/New directory to move")
        ap = input()
        os.system("mv " + ao + " " + ap)
    elif m == 11:
        print("Write full path to file")
        aq = input()
        print("Full path to new directory")
        ar = input()
        os.system("cp " + aq + " " + ar)
    elif m == 12:
        print("Write full path to directory")
        au = input()
        print("Full path to new directory")
        at = input()
        os.system("cp -r " + au + " " + at)
    elif m == 13:
        os.system("mc")
    elif m == 14:
        x = PrettyTable()
        x.field_names = ["N", "Option"]
        x.add_rows(
           [
               [1, "chmod"],
               [2, "chattr"],
           ]
        )
        print(x)
        aw = int(input())
        print("Write options and file")
        ax = input()
        
        if aw == 1:
            os.system("chmod " + ax)
        elif aw == 2:
            os.system("chattr " + ax)
    elif m == 15:
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    time.sleep(10)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Terminal tools':
    os.system("python3 /data/data/com.termux/files/chroot/terminal.py")
elif a == 'Help for STALIN-OS':
    os.system("termux-open /data/data/com.termux/files/system/help.html")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'PVI':
    os.system("vim /data/data/com.termux/files/home/.vimrc")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'System menu':
    os.system("python3 /data/data/com.termux/files/boot/login.py")
    os.system("clear && python3 /data/data/com.termux/files/system/setting.py")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Tor':
    os.system("tor")
    print("Ctrl-Z for stopping")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'For developers':
    os.system("termux-open /data/data/com.termux/files/system/fordev.html")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Open':
    print("Path to file (full path)")
    j = input()
    os.system("termux-open " + j)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Calculator':
    os.system("clear && calc")
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'GRUB':
    os.system("clear && python3 /data/data/com.termux/files/boot/grub.py")
elif a == 'TNS':
    os.system("clear")
    os.system("ping 8.8.8.8")
    time.sleep(10)
    os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'OFTE':
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Editor"]
    x.add_rows(
        [
            [1, "nano"],
            [2, "vim"],
            [3, "micro"],
            [4, "neovim"],
            [5, "joe"],
            [6, "emacs"],
            [7, "mcedit"],
            [8, "System editor"],
            [9, "vi"],
            [10, "exit"],
        ]
    )
    print(x)
    print("Select your editor:")
    k = int(input())
    print("Full path to file:")
    l = input()

    if k == 1:
        os.system("nano " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 2:
        os.system("vim " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 3:
        os.system("micro " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 4:
        os.system("neovim " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 5:
        os.system("joe " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 6:
        os.system("emacs " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 7:
        os.system("mcedit " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 8:
        os.system("termux-open " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 9:
        os.system("vi " + l)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif k == 10:
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
elif a == 'Run SSH':
    print(colored("Write user:", 'grey', 'on_white'))
    ah = input()
    print(colored("Write host IP", 'grey', 'on_white'))
    ai = input()
    print(colored("Write host port (default port is 22, write even it)", 'grey', 'on_white'))
    aj = input()
    os.system("ssh " + ah + "@" + ai + " -p" + aj)
    os.system("python3 /data/data/com.termux/files/chroot/chroot.py")
