#!/bin/bash
nimloc=$(command -v nimble)
if [ -x "$nimloc" ]; then
  exit
fi

curl https://nim-lang.org/choosenim/init.sh -sSf | sh

if [ "$OSTYPE" == "darwin*" ]; then
	scode-select --install
fi

