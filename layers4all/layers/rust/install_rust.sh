#!/bin/bash
rustup=$(command -v rustup)

if [ -x "$rustup" ]; then
  exit
fi

if [ "$OSTYPE" == "linux*" ]; then
  apt install libssl-dev
fi

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup-init
rustup update
cargo install cargo-edit
rustup component add rls rust-analysis rust-src
