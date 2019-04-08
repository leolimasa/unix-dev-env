#!/usr/bin/env python3
from os import path
import pathlib
import os
import sys
import subprocess
import re


def lang_typescript():
    os.system('npm install -g javascript-typescript-langserver')
    server = subprocess.check_output(
        ['which', 'javascript-typescript-stdio']).decode('UTF-8')
    return {'LANGSERVER_TS': server}


def lang_python():
    os.system("pip3 install 'python-language-server[all]'")
    os.system("pip3 install pynvim")
    server = subprocess.check_output(['which', 'pyls']).decode('UTF-8')
    return {'LANGSERVER_PY': server}


def lang_go():
    pass


def lang_css():
    os.system("npm install --global vscode-css-languageserver-bin")
    server = subprocess.check_output(
        ['which', 'css-languageserver']).decode('UTF-8')
    return {'LANGSERVER_CSS': server}


def lang_bash():
    os.system("npm i -g bash-language-server")
    server = subprocess.check_output(
        ['which', 'bash-language-server']).decode('UTF-8')
    return {'LANGSERVER_BASH': server}

def lang_rust():
    os.system("rustup update")
    os.system("rustup component add rls rust-analysis rust-src")
    server = subprocess.check_output(
        ['which', 'rustup']).decode('UTF-8')
    return {'LANGSERVER_RUST': server}

def lang_json():
    pass


def lang_yaml():
    pass


def lang_html():
    pass


def lang_csharp():
    pass


def lang_dockerfile():
    pass


def lang_xml():
    pass




langs = {'typescript': lang_typescript,
        'python': lang_python, 'css': lang_css, 'bash': lang_bash, 'rust': lang_rust}

DEVENV_START = '# Unix dev env START'
DEVENV_END = '# Unix dev env END'


def bash_lines(dir: str, envvars: dict) -> str:
    env = '\n'.join([f'export {k}={envvars[k]}' for k in envvars])
    return '\n'.join([
        DEVENV_START,
        f'export PATH=$PATH:{path.join(dir, "bin")}',
        f'source {dir}/bashrc',
        env,
        DEVENV_END
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


def remove_devenv_section_from_file(path: str):
    # Create regular expression pattern
    chop = re.compile(f'{DEVENV_START}.*?{DEVENV_END}', re.DOTALL)

    # Open file
    f = open(path, 'r')
    data = f.read()
    f.close()

    # Chop text between #chop-begin and #chop-end
    data_chopped = chop.sub('', data)

    # Save result
    f = open(path, 'w')
    f.write(data_chopped)
    f.close()


def replace_in_file(path: str, contents: str):
    remove_devenv_section_from_file(path)
    append_to_file(path, contents)


def setup_vim(repo_dir: str, home: str):
    # Needed for deoplete
    os.system('pip3 install pynvim')

    append_to_file(path.join(home, ".vimrc"), vimrc_lines(repo_dir))

    # Download plug
    plug_vim = path.join(home, ".vim", "autoload", "plug.vim")
    os.system(
        f"curl -fLo {plug_vim} --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim")

    # Install plugins
    os.system("vim +PlugInstall +qall")

    # Compiles YCM
    #install_py = path.join(home, ".vim", "plugged", "youcompleteme", "install.py")
    #os.system(f'{install_py} --clang-completer --cs-completer --go-completer --java-completer')


def setup_bashrc(repo_dir: str, home: str, env: dict):
    print(bash_lines(repo_dir, env))
    replace_in_file(path.join(home, ".bash_profile"),
                    bash_lines(repo_dir, env))
    replace_in_file(path.join(home, ".bashrc"), bash_lines(repo_dir, env))


def setup_env(languages):
    return install_langs(languages)


def vim_as_git_diff():
    os.system("git config merge.tool vimdiff")
    os.system("git config merge.conflictstyle diff3")
    os.system("git config mergetool.prompt false")


def install_langs(languages):
    result = {}
    for lang in languages:
        result.update(langs[lang]())
    return result


def install(languages, repo_dir: str, home: str):
    os.system("brew install vim --override-system-vi --with-client-server")
    env = setup_env(languages)
    setup_bashrc(repo_dir, home, env)
    append_to_file(path.join(home, ".tmux.conf"), tmux_lines(repo_dir))
    setup_vim(repo_dir, home)
    vim_as_git_diff()


def home():
    return str(pathlib.Path.home())


def repo_dir():
    return path.dirname(path.abspath(__file__))


def retrieve_langs():
    return ["typescript", "python", "css", "bash", "rust"]


if __name__ == "__main__":
    if len(sys.argv) > 0:
        if sys.argv[1] == "vim":
            setup_vim(repo_dir(), home())
        elif sys.argv[1] == "bashrc":
            setup_bashrc(repo_dir(), home(), setup_env(retrieve_langs()))
    else:
        install(retrieve_langs, repo_dir(), home())
