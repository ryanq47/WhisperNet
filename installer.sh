#!/bin/bash

echo "####################"
echo "Logec Installer!"
echo "####################"

echo "##=================="
echo "Checking for updates..."
echo "##=================="
sudo apt-get update -y


echo "##=================="
echo "Installing Requirments..."
echo "##=================="

pip install -r requirements.txt


echo "##=================="
echo "Installing Additional PyQt Stuff..."
echo "##=================="
#sudo apt-get install python3-pyqt5.qtsql



## Adding path so it can be read by pyqt GUI - need to refine this later
echo "=================="
echo "All done!"
echo "##=================="
