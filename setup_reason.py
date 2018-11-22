#!/usr/bin/env python3
from setup import append_to_file, repo_dir, home
from os import path

def setup_vim(repo_dir: str, home: str):
    reason_server = path.join(repo_dir, "reason-language-server-mac", "reason-language-server.exe")
    vimrc = ("\ncall plug#begin('~/.vim/plugged')\n"
            "Plug 'reasonml-editor/vim-reason-plus'\n"
            "Plug 'autozimu/LanguageClient-neovim', {\n"
            "\ 'branch': 'next',\n"
            "\ 'do': 'bash install.sh',\n"
            "\ }\n"
            "Plug 'Shougo/deoplete.nvim'\n"
            "call plug#end()\n"
            "\n"
            "let g:LanguageClient_serverCommands = {\n"
            f"\ 'reason': ['{reason_server}'],\n"
            "\ }\n"
            )
    append_to_file(path.join(home, ".vimrc"), vimrc)

if __name__ ==  "__main__":
    setup_vim(repo_dir(), home())
