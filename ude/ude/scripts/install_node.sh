#!/usr/bin/env bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
. $HOME/.nvm/nvm.sh  # This loads NVM
nvm install stable
nvm use node
