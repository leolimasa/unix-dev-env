#!/usr/bin/env python3
from os import path
import pathlib
import os

def bash_lines(dir: str) -> str:
    return '\n'.join([
        f'# Unix dev env',
        f'export PATH=$PATH:{path.join(dir, "bin")}',
        f'source {dir}/bashrc'
        ])

def tmux_lines(dir: str) -> str:
    return '\n'.join([
        f'source-file {path.join(dir, "tmux.conf")}'
        ])

def vimrc_lines(dir: str) -> str:
    return '\n'.join([
        f'so {path.join(dir, "vimrc")}'
        ])


def append_to_file(path: str, contents: str):
    f = open(path, "a" if os.path.exists(path) else "w+")
    f.write(contents)
    f.close()

def setup_vim(home: str):
    # Download plug
    plug_vim = path.join(home, ".vim", "autoload", "plug.vim")
    os.system(f"curl -fLo {plug_vim} --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim")

    # Install plugins
    os.system("vim +PlugInstall +qall")

    # Compiles YCM
    install_py = path.join(home, ".vim", "plugged", "youcompleteme", "install.py")
    os.system(f'{install_py} --clang-completer --cs-completer --go-completer --java-completer')

def install(repo_dir: str, home: str):
    append_to_file(path.join(home, ".bash_profile"), bash_lines(repo_dir))
    append_to_file(path.join(home, ".tmux.conf"), tmux_lines(repo_dir))
    append_to_file(path.join(home, ".vimrc"), vimrc_lines(repo_dir))
    setup_vim(home)

if __name__ == "__main__":
    home = str(pathlib.Path.home())
    repo_dir = path.dirname(path.abspath(__file__))
    install(repo_dir, home)
