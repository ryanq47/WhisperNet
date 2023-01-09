#!/bin/bash

echo "####################"
echo "Logec Installer!"
echo "####################"

echo "##=================="
echo "Installing PipReqs..."
echo "##=================="

pip install -r requirements.txt


## Adding path so it can be read by pyqt GUI - need to refine this later
program_path=$(pwd)
#pwd > .syspath
echo "path = '$program_path'" > syspath.py


echo "##=================="
echo "Adding to path..."
echo "##=================="

echo "Enter Shell file (.bashrc, .zshrc, etc -- INCLUDE THE '.'!)"
read SHELLFILE

echo 'export PATH="'$program_path'/:$PATH"' >> ~/$SHELLFILE

#echo "'export PATH=$program_path:$PATH'" >> ~/.$SHELLFILE

echo "##=================="
echo "All done! Reboot for the new path to take effect. Then run ./logec-attack.py to start the program!"
echo "##=================="
