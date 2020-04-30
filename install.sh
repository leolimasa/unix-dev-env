#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
	apt-get -y install python3.7
	apt-get -y install python3-pip
	apt-get -y install fish
	apt-get -y install neovim
	apt-get -y install git
	apt-get -y install curl
	apt-get -y install tmux
	pip3 install pipenv
elif [[ "$OSTYPE" == "darwin"* ]]; then
	brew install tmux
	brew install fish
	brew install neovim
	brew install python3
	brew install git
	pip3 install pipenv
fi

# Install node (coc relies on it)
if ! [ -x "$(command -v node)" ]; then
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
	. $HOME/.nvm/nvm.sh  # This loads NVM
	nvm install stable
	nvm use node
fi

mkdir -p ~/Projects/Sandbox

# Clone layers4all
cd ~/Projects/Sandbox
git clone https://github.com/leolimasa/layers4all.git

# TODO Set fish as default shell 


# TODO apply l4a standard configs
