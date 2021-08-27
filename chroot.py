#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

print("============================")
print(colored("Contacts", 'red', 'on_grey'))
print("----------------------------")
print(colored("Music", 'red', 'on_grey'))
print("----------------------------")
print(colored("Package Manager", 'cyan', 'on_grey'))
print("----------------------------")
print(colored("Games", 'red', 'on_grey'))
print("----------------------------")
print(colored("Taskmgr Linux (Taskmgr)", 'red', 'on_grey'))
print("----------------------------")
print(colored("Telegram [supported for arm64]", 'red', 'on_grey'))
print("----------------------------")
print(colored("File Manager", 'cyan', 'on_grey'))
print("----------------------------")
print(colored("Terminal tools", 'green', 'on_grey'))
print("----------------------------")
print(colored("System menu", 'magenta' ,'on_grey'))
print("----------------------------")
print(colored("Help for STALIN-OS", 'magenta', 'on_grey'))
print("----------------------------")
print(colored("Plugin Vim Install (PVI)", 'green', 'on_grey'))
print("----------------------------")
print(colored("Tor", 'magenta', 'on_grey'))
print("----------------------------")
print(colored("For developers", 'yellow', 'on_grey'))
print("----------------------------")
print(colored("Open file in android app (Open)", 'red', 'on_grey'))
print("----------------------------")
print(colored("Calculator", 'green', 'on_grey'))
print("----------------------------")
print(colored("Test network speed (TNS)", 'yellow', 'on_grey'))
print("----------------------------")
print(colored("Open file into text editor (OFTE)", 'red', 'on_grey'))
print("----------------------------")
print(colored("Run SSH", 'cyan', 'on_grey'))
print("----------------------------")
print(colored("Exit to GRUB (GRUB)", 'cyan', 'on_grey'))
print("============================")
print(colored("Run app:", 'grey', 'on_blue'))
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
    print(colored("What do you want to do?", 'cyan', 'on_grey'))
    print(colored("1.Check files", 'cyan', 'on_grey'))
    print(colored("2.Check all info for files", 'cyan', 'on_grey'))
    print(colored("3.Check attributes of files", 'cyan', 'on_grey'))
    print(colored("4.Find file in directory", 'cyan', 'on_grey'))
    print(colored("5.Execute file", 'cyan', 'on_grey'))
    print(colored("6.Make directory", 'cyan', 'on_grey'))
    print(colored("7.Make file", 'cyan', 'on_grey'))
    print(colored("8.Remove file/directory", 'cyan', 'on_grey'))
    print(colored("9.Totally remove file/directory", 'cyan', 'on_grey'))
    print(colored("10.Move/Rename file/directory", 'cyan', 'on_grey'))
    print(colored("11.Copy file", 'cyan', 'on_grey'))
    print(colored("12.Copy directory", 'cyan', 'on_grey'))
    print(colored("13.Run file checker", 'cyan', 'on_grey'))
    print(colored("14.chmod/chattr", 'cyan', 'on_grey'))
    print(colored("15.Exit to chroot", 'cyan', 'on_grey'))
    print(colored("====================", 'cyan', 'on_grey'))
    print(colored("Select your function", 'green', 'on_grey'))
    m = int(input())
    
    if m == 1:
        print(colored("Directory:", 'cyan', 'on_grey'))
        ae = input()
        os.system("ls -a " + ae)
    elif m == 2:
        print(colored("Directory:", 'cyan', 'on_grey'))
        af = input()
        os.system("ls -al " + af)
    elif m == 3:
        print(colored("Directory:", 'cyan', 'on_grey'))
        ag = input()
        os.system("lsattr " + ag)
    elif m == 4:
        print(colored("File name for find:", 'green', 'on_grey'))
        n = input()
        print(colored("Directory where find:", 'green', 'on_grey'))
        o = input()
        os.system("ls -a " + o + " | grep " + n)
    elif m == 5:
        os.system("clear")
        print(colored("1.Run bash script", 'red', 'on_grey'))
        print(colored("2.Run python2 script", 'red', 'on_grey'))
        print(colored("3.Run python3 script", 'red', 'on_grey'))
        print(colored("4.Run ruby script", 'red', 'on_grey'))
        print(colored("5.Run makefile", 'yellow', 'on_grey'))
        print(colored("6.Run compiled C/C++/Rust script", 'red', 'on_grey'))
        print(colored("7.Run go-lang script", 'red', 'on_grey'))
        print(colored("8.Compile java program", 'yellow', 'on_grey'))
        print(colored("9.Run java program", 'red', 'on_grey'))
        print(colored("10.Run php program", 'red', 'on_grey'))
        print(colored("11.Run swift program", 'red', 'on_grey'))
        print(colored("12.Compile rust program", 'yellow', 'on_grey'))
        n = int(input())
        
        if n == 1:
            print(colored("Write path to script and parameters", 'green', 'on_grey'))
            o = input()
            os.system("bash " + o)
        elif n == 2:
            print(colored("Write path to script and parameters", 'green', 'on_grey'))
            p = input()
            os.system("python2 " + p)
        elif n == 3:
            print(colored("Write path to script and parameters", 'green', 'on_grey'))
            q = input
            os.system("python3 " + q)
        elif n == 4:
            print(colored("Write path to script and parameters", 'green', 'on_grey'))
            r = input()
            os.system("ruby " + r)
        elif n == 5:
            print(colored("Print directory with script", 'cyan', 'on_grey'))
            s = input()
            os.system("cd " + s)
            print(colored("Print parameters or scriptname (if test.cpp, then write \"test\")", 'green', 'on_grey'))
            t = input()
            os.system("make " + t)
        elif n == 6:
            print(colored("Write script directory", 'green', 'on_grey'))
            u = input()
            os.system("cd " + u)
            print(colored("Write script name", 'green', 'on_grey'))
            v = input()
            os.system("./" + v)
        elif n == 7:
            print(colored("Write script (full path)", 'green', 'on_grey'))
            w = input()
            os.system("go run " + w)
        elif n == 8:
            print(colored("Write script directory", 'green', 'on_grey'))
            x = input()
            os.system("cd " + x)
            print(colored("Write script name (if namescript is test.java, write \"test\"", 'green', 'on_grey'))
            y = input()
            os.system("javac " + y)
        elif n == 9:
            print(colored("Full path to script", 'green', 'on_grey'))
            z = input()
            os.system("java " + z)
        elif n == 10:
            print(colored("Full path to script", 'green', 'on_grey'))
            aa = input()
            os.system("php " + aa)
        elif n == 11:
            print(colored("Full path to script", 'green', 'on_grey'))
            ab = input()
            os.system("swift " + ab)
        elif n == 12:
            print(colored("Print working directory", 'green', 'on_grey'))
            ac = input()
            os.system("cd " + ac)
            print(colored("Script name (if the filename is test.rust, write \"test\"", 'green', 'on_grey'))
            ad = input()
            os.system("rustc " + ad)
        time.sleep(5)
        os.system("clear && python3 /data/data/com.termux/files/chroot/chroot.py")
    elif m == 6:
        print(colored("Write full path to new directory", 'green', 'on_grey'))
        ak = input()
        os.system("mkdir " + ak)
    elif m == 7:
        print(colored("Write full path to new file", 'green', 'on_grey'))
        al = input()
        os.system("touch " + al)
    elif m == 8:
        print(colored("Write full path to file/directory", 'green', 'on_grey'))
        am = input()
        os.system("rm -rf " + am)
    elif m == 9:
        print(colored("Write full path to file/directory", 'green', 'on_grey'))
        an = input()
        os.system("shred -n 10 " + an)
    elif m == 10:
        print(colored("Write full old path to file/directory", 'green', 'on_grey'))
        ao = input()
        print(colored("Full path with new name/New directory to move", 'green', 'on_grey'))
        ap = input()
        os.system("mv " + ao + " " + ap)
    elif m == 11:
        print(colored("Write full path to file", 'green', 'on_grey'))
        aq = input()
        print(colored("Full path to new directory", 'green', 'on_grey'))
        ar = input()
        os.system("cp " + aq + " " + ar)
    elif m == 12:
        print(colored("Write full path to directory ", 'green', 'on_grey'))
        au = input()
        print(colored("Full path to new directory", 'green', 'on_grey'))
        at = input()
        os.system("cp -r " + au + " " + at)
    elif m == 13:
        os.system("mc")
    elif m == 14:
        print(colored("1.chmod", 'green', 'on_grey'))
        print(colored("2.chattr", 'green', 'on_grey'))
        aw = int(input())
        print(colored("Write options and file", 'green', 'on_grey'))
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
    print(colored("| === === === === |", 'yellow', 'on_grey'))
    print(colored("| 1.nano          |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 2.vim           |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 3.micro         |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 4.neovim        |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 5.joe           |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 6.emacs         |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 7.mcedit        |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 8.System editor |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 9.vi            |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 10.exit         |", 'yellow', 'on_grey'))
    print(colored("| === === === === |", 'yellow', 'on_grey'))
    print(colored("Select your editor:", 'green', 'on_grey'))
    k = int(input())
    print(colored("Full path to file:", 'green', 'on_grey'))
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
