#!/bin/bash

VENV_NAME=".venv_l"
# I used python 3.13 and 3.12 (by accident whoops) which both work but any python version that supports the dependencies should work
# This script is kinda just like a docker file lowkey... (not building one for windows)
# Works on WSL and Linux, although you may need something like dos2unix
# this is becuase I wrote this on a windows machine and bash does not like CLRF (Usually uses LF)
# Can be fixed with dos2unix (sudo apt install dos2unix) (sudo pacman -S dos2unix)
# run dos2unix L_env.sh to change from CRLF to LF 
if [ -d $VENV_NAME ]; then
    echo "Virtual environment already exists."
else
    echo "Creating virtual environment..."
    python3 -m venv $VENV_NAME
    echo "Sucessfully created virtual environment"
fi

source $VENV_NAME/bin/activate
pip install -r backend/requirements.txt
pip install gunicorn


echo "Now run:"
echo "source $VENV_NAME/bin/activate"
echo "to activate the virtual environment in the current terminal" 

