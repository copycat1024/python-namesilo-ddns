#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd $DIR
pyvenv py_env
source py_env/bin/activate
pip install -r requirements.txt
chmod +x run.sh
