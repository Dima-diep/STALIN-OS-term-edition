#!/bin/bash
clear
ECHO() {
clear;
echo "STALIN-OS 2.8.0 term edition uninstaller";
echo "Uninstalling system...";
}
ECHO
echo "(--------------------)"
echo "0%"
echo "#!/bin/bash" > /data/data/com.termux/files/usr/bin/login
echo "cat ~/../usr/etc/motd" >> /data/data/com.termux/files/usr/bin/login
echo "bash" >> /data/data/com.termux/files/usr/bin/login
ECHO
echo "(##------------------)"
echo "10%"
rm -rf /data/data/com.termux/files/boot
ECHO
echo "(####----------------)"
echo "20%"
rm -rf /data/data/com.termux/files/chroot
ECHO
echo "(######--------------)"
echo "30%"
rm -rf /data/data/com.termux/files/.initialize
ECHO
echo "(########------------)"
echo "40%"
rm -rf /data/data/com.termux/files/.recovery
ECHO
echo "(##########----------)"
echo "50%"
rm -rf /data/data/com.termux/files/system
ECHO
echo "(############--------)"
echo "60%"
rm -rf /data/data/com.termux/files/home/Music-Termux
ECHO
echo "(##############------)"
echo "70%"
rm -rf /data/data/com.termux/files/home/.bashrc
ECHO
echo "(################----)"
echo "80%"
rm -rf /data/data/com.termux/files/home/Linux-Installer-Termux
ECHO
echo "(##################--)"
echo "90%"
mv /data/data/com.termux/files/home/.bashrc.old /data/data/com.termux/files/home/.bashrc
ECHO
echo "(###################-)"
echo "95%"
rm -rf /data/data/com.termux/files/home/STALIN-OS-term-edition
ECHO
echo "(####################)"
echo "100%"
sleep 2
clear
