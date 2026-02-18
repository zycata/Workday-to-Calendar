#!/bin/bash

VENV_NAME=".venv_wsl"
# This script is created for using wsl (windows subsystem for linux) to create an environment on windows machines
# this also works for regular linux too
if [ -d $VENV_NAME ]; then
    echo "Virtual environment already exists."
else
    echo "Creating virtual environment..."
    python3 -m venv $VENV_NAME
    echo "Sucessfully created virtual environment"
fi




echo "Now run:"
echo "source $VENV_NAME/bin/activate"
echo "pip install -r backend/requirements.txt"
echo "pip install gunicorn"

