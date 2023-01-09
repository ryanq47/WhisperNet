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


