#!/bin/bash

VENV_NAME=".venv_l"
# This script is created for using wsl (windows subsystem for linux) to create an environment on windows machines
# this also works for regular linux too
# pretty cool huh? no automated install for windows or anything because uhh boo 
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

