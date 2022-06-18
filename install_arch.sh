#!/bin/bash
clear
echo "Installing Arch Script..."
sudo pacman -S python3 figlet python2-pip python3-pip python-pip gnome-terminal -y
pip install colorama
pip3 install colorama
echo "Installed!"
chmod 777 llot
echo "Use ./llot to execute the script"
exit