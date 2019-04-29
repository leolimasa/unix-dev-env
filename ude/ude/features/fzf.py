from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, install_package
from os import path
import platform


def setup(env: UdeEnvironment) -> UdeFeature:
    try:
        run_cmd(['which', 'fzf'])
    except:
        if platform.system() == 'Linux':
            setup_linux(env)
        elif platform.system() == 'Darwin':
            run_cmd(['brew', 'install', 'fzf'])
        else:
            raise Exception(f'Fzf not supported on {platform.system()}')
    return UdeFeature(
            name='fzf',
            envs={},
            post_install=None
            )

def setup_linux(env: UdeEnvironment) -> None:
    run_cmd(['git','clone','--depth','1',
        'https://github.com/junegunn/fzf.git',
        path.join(env.home_dir, ".fzf")])
    run_cmd(['~/.fzf/install'])

