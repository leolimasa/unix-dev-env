#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Install python so we can run the script
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	if ! [ -x "$(command -v python3.7)" ]; then
		apt install python3.7
		apt install python3-setuptools
		apt install python3.7-venv
		apt install python3-pip
		pip3 install wheel
	fi
#elif [[ "$OSTYPE" == "darwin"* ]]; then
# TODO install python3.2 on macos if it doesn't exist
fi

# Node is required for Coc, so we always check for it.
if ! [ -x "$(command -v node)" ]; then
	source $DIR/ude/ude/scripts/install_node.sh
fi

cd $DIR/ude
python3.7 -m venv venv
venv/bin/python3.7 setup.py develop
venv/bin/python3.7 -m ude.install
echo "Installation done. If this is the first time you install, quit and reenter the terminal."
