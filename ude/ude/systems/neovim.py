from os import path
import os
from ..model import UdeEnvironment
from ..fs import write_template, rewrite_file_block, run_cmd, install_package


def setup(env: UdeEnvironment) -> None:
    try:
        run_cmd(['which', 'nvim'])
    except:
        install_package('neovim')
    try:
        run_cmd(['which', 'yarn'])
    except:
        os.system('curl -o- -L https://yarnpkg.com/install.sh | bash')
    write_template('neovim.vim', env)
    rewrite_file_block(
        '" UDE-START\n',
        '" UDE-END\n',
        path.join(env.home_dir, '.config', 'nvim', 'init.vim'),
        f'source {env.ude_config_dir}/neovim.vim\n')
    install_plug(env)
    run_cmd([
        'nvim',
        '+PlugInstall',
        '+UpdateRemotePlugins',
        '+qall'])
    setup_coc(env)
    vim_as_git_diff()


def setup_coc(env: UdeEnvironment) -> None:
    write_template('coc-settings.json', env,
                   os.path.join(env.home_dir, '.config', 'nvim', 'coc-settings.json'))
    run_cmd([
        'nvim',
        '"+CocInstall coc-json"',
        '"+CocInstall coc-html"',
        '"+CocInstall coc-css"',
        '"+CocInstall coc-highlight"',
        '"+CocInstall coc-yaml"',
        '+qall'])

def vim_as_git_diff() -> None:
    os.system("git config merge.tool nvim -d")
    os.system("git config merge.conflictstyle diff3")
    os.system("git config mergetool.prompt false")

def install_plug(env: UdeEnvironment) -> None:
    plug_dir = path.join(
        env.home_dir, '.local', 'share', 'nvim', 'site', 'autoload', 'plug.vim')
    if path.exists(plug_dir):
        return
    run_cmd([
        'curl',
        '-fLo',
        plug_dir,
        '--create-dirs',
        'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
    ])
