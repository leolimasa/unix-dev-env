#!/bin/bash
fzfloc=$(command -v fzf)

if [ -x "$fzfloc" ]; then
  exit
fi

if [ "$OSTYPE" == "darwin*" ]; then
  brew install fzf
fi

if [ "$OSTYPE" == "linux*" ]; then
  git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
  ~/.fzf/install
fi
