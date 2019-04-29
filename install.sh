#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	apt install python3.7
	apt install python3-setuptools
	apt install virtualenv
#elif [[ "$OSTYPE" == "darwin"* ]]; then
# ...
fi

cd $DIR/ude
python3.7 -m venv venv
venv/bin/python3.7 setup.py develop
venv/bin/python3.7 -m ude.install
