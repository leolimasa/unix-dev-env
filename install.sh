#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/ude
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	apt install python3.7
	apt install python3-setuptools
	apt install virtualenv
	virtualenv venv
	
elif [[ "$OSTYPE" == "darwin"* ]]; then
	# ...
fi

python3.7 setup.py develop
python3.7 -m ude.install
