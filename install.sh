#!/bin/bash
ECHO() {
clear;
echo "STALIN-OS term edition v2.8.1 installer";
echo "Installing system...";
}
termux-setup-storage
ECHO
echo "(-------------------------)"
echo "0%"
chmod 777 *.py *.sh *.html
ECHO
echo "(-------------------------)"
echo "2%"
apt update -y &>/dev/null
ECHO
echo "(#------------------------)"
echo "4%"
apt upgrade -y &>/dev/null
ECHO
echo "(#------------------------)"
echo "6%"
apt install python termux-api mpv htop-legacy tor libc++ wget calc openssh mc man proot proot-distro -y &>/dev/null
ECHO
echo "(##-----------------------)"
echo "8%"
python3 -m pip install --upgrade pip >/dev/null
ECHO
echo "(##-----------------------)"
echo "10%"
python3 -m pip install requests tqdm PTable urllib3 charset-normalizer certifi idna prettytable wcwidth >/dev/null
ECHO
echo "(###----------------------)"
echo "12%"
apt remove zsh -yq &>/dev/null
ECHO
echo "(###----------------------)"
echo "14%"
apt autoremove -yq &>/dev/null
ECHO
echo "(####---------------------)"
echo "16%"
rm -rf /data/data/com.termux/files/home/.oh-my-zsh
ECHO
echo "(####---------------------)"
echo "18%"
rm -rf /data/data/com.termux/files/home/.zshrc
ECHO
echo "(#####--------------------)"
echo "20%"
mv /data/data/com.termux/files/home/.bashrc /data/data/com.termux/files/home/.bashrc.old
ECHO
echo "(#####--------------------)"
echo "22%"
cd /data/data/com.termux/files
mkdir boot
ECHO
echo "(######-------------------)"
echo "24%"
mkdir chroot
ECHO
echo "(######-------------------)"
echo "26%"
mkdir system
ECHO
echo "(#######------------------)"
echo "28%"
mkdir .initialize
ECHO
echo "(#######------------------)"
echo "30%"
cd ../home/STALIN-OS-term-edition
mv grub.py ../../boot
ECHO
echo "(########-----------------)"
echo "32%"
mv *.mp3 ../../boot
ECHO
echo "(########-----------------)"
echo "34%"
mv login.py ../../boot
ECHO
echo "(#########----------------)"
echo "36%"
mv pass.py ../../boot
ECHO
echo "(#########----------------)"
echo "38%"
mv chlogin.py ../../chroot
ECHO
echo "(##########---------------)"
echo "40%"
mv chpass.py ../../chroot
ECHO
echo "(##########---------------)"
echo "42%"
mv chroot.py ../../chroot
ECHO
echo "(###########--------------)"
echo "44%"
mv pacman.py ../../chroot
ECHO
echo "(###########--------------)"
echo "46%"
mv setting.py ../../system
ECHO
echo "(############-------------)"
echo "48%"
mv terminal.py ../../chroot
ECHO
echo "(############-------------)"
echo "50%"
mv initialize.* ../../.initialize
ECHO
echo "(#############------------)"
echo "54%"
mv help.* ../../system
ECHO
echo "(##############-----------)"
echo "56%"
mv uninstall.* ../../system
ECHO
echo "(###############----------)"
echo "60%"
mv boot.py ../../boot
ECHO
echo "(###############----------)"
echo "62%"
mv fordev.html ../../system
ECHO
echo "(################---------)"
echo "64%"
mv Manifest.json ../../system
ECHO
echo "(################---------)"
echo "66%"
mv recovery.py ../../system
ECHO
echo "(#################--------)"
echo "68%"
mv atilo ../../usr/bin
ECHO
echo "(#################--------)"
echo "70%"
chmod 777 *
ECHO
echo "(##################-------)"
echo "72%"
echo "#!/bin/bash" > ../../usr/bin/login
echo "python3 /data/data/com.termux/files/boot/grub.py" >> ../../usr/bin/login
ECHO
echo "(##################-------)"
echo "74%"
cd ../../chroot
touch contacts.txt
ECHO
echo "(###################------)"
echo "76%"
cd ../system
touch .killhist.sh
ECHO
echo "(###################------)"
echo "78%"
chmod 777 .killhist.sh
ECHO
echo "(####################-----)"
echo "80%"
echo "#!/bin/bash" > .killhist.sh
echo "rm -rf ~/.bash_history" >> .killhist.sh
echo "rm -rf ~/.zsh_history" >> .killhist.sh
echo "rm -rf ~/.wget_hsts" >> .killhist.sh
echo "rm -rf ~/.python_history" >> .killhist.sh
echo "rm -rf ~/.sqlite_history" >> .killhist.sh
ECHO
echo "(####################-----)"
echo "82%"
cd ../home
touch .bashrc
ECHO
echo "(#####################----)"
echo "84%"
git clone https://github.com/Dima-diep/Linux-Installer-Termux &>/dev/null
ECHO
echo "(######################---)"
echo "89%"
git clone https://github.com/Dima-diep/Music-Termux &>/dev/null
ECHO
echo "(#######################--)"
echo "94%"
chmod 777 Music-Termux/*
ECHO
echo "(########################-)"
echo "96%"
chmod 777 Linux-Installer-Termux/*
ECHO
echo "(########################-)"
echo "98%"
chsh -s bash
ECHO
echo "(#########################)"
echo "100%"
sleep 2
clear
echo "Your system login is oldlogin"
echo "Your system password is oldpass"
echo "STALIN-OS has been installed. Restart Termux App for starting OS!"
echo "Until reboot, uninstall any zsh plugins from system because operating system isn't compatible with zsh"
