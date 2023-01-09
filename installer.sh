#!/bin/bash

echo "####################"
echo "Logec Installer!"
echo "####################"

echo "##=================="
echo "Checking for updates..."
echo "##=================="


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

SHELLFILE_CHECK='export PATH="'$program_path'/:$PATH"'

if grep -Fxq "$SHELLFILE_CHECK" ~/$SHELLFILE
then
	echo "Already in $SHELLFILE, passing"
else
	echo 'export PATH="'$program_path'/:$PATH"' >> ~/$SHELLFILE
	echo "Successfully added to '$SHELLFILE'..."
fi


echo "##=================="
echo "All done! Reboot for the new path to take effect. Then run ./logec-attack.py to start the program!"
echo "##=================="
