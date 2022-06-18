#!/bin/bash
clear
echo "Installing..."
sudo apt install python3 figlet python2-pip python3-pip python-pip gnome-terminal -y
pip3 install colorama
pip install colorama
echo "Installed!"
chmod 777 llot
echo "Use ./llot to execute the script"
