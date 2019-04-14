
from os import path
import os
from ..model import UdeEnvironment
from ..fs import write_template, rewrite_file_block, run_cmd, install_package

def setup(env: UdeEnvironment):
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

def setup_coc(env: UdeEnvironment):
    write_template('coc-settings.json', env,
            os.path.join(env.home_dir, '.config', 'nvim', 'coc-settings.json'))
    run_cmd([
        'nvim',
        '"+CocInstall coc-json"',
        '+qall'])

def install_plug(env: UdeEnvironment):
    plug_dir = path.join(
        env.home_dir, '.local', 'share', 'nvim', 'site', 'autoload', 'plug.vim')
    run_cmd([
        'curl',
        '-fLo',
        plug_dir,
        '--create-dirs',
        'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
    ])
