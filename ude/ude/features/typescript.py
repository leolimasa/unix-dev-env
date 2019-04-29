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
            os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash')
            os.system('export NVM_DIR=~/.nvm')
            os.system('sh ~/.nvm/nvm.sh')
            os.system('export NVM_DIR=~/.nvm; sh ~/.nvm/nvm.sh;nvm install stable')
    run_cmd(['npm', 'install', '-g', 'javascript-typescript-langserver'])
    return UdeFeature(
        name='typescript',
        envs={},
        post_install=post_install
    )

def post_install(env: UdeEnvironment) -> None:
    run_cmd(['nvim', '"+CocInstall coc-tsserver"', '+qall'])
