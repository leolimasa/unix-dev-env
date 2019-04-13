from os import path
from ..model import UdeEnvironment
from ..fs import write_template, rewrite_file_block, run_cmd


def setup(env: UdeEnvironment):
    run_cmd(['brew', 'install', 'neovim'])
    write_template('neovim.vim', env)
    rewrite_file_block(
        '" UDE-START',
        '" UDE-END',
        path.join(env.home_dir, '.config', 'nvim', 'init.vim'),
        f'source {env.ude_config_dir}/neovim.vim')
