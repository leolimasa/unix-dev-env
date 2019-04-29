from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd
import platform
import os

def setup(env: UdeEnvironment) -> UdeFeature:
    try:
        run_cmd(['which','node'])
    except:
        # TODO add OSX installation here as well (which is a PITA)
        if platform.system() == 'Linux':
            os.system('apt install nodejs')
            os.system('apt install npm')
    run_cmd(['npm', 'install', '-g', 'javascript-typescript-langserver'])
    return UdeFeature(
        name='typescript',
        envs={},
        post_install=post_install
    )

def post_install(env: UdeEnvironment) -> None:
    run_cmd(['nvim', '"+CocInstall coc-tsserver"', '+qall'])
