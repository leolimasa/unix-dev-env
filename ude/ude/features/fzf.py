from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, install_package
import platform

def setup(env: UdeEnvironment) -> UdeFeature:
    try:
        run_cmd(['which', 'fzf'])
    except:
        if platform.system() == 'Linux':
            setup_linux()
        elif platform.system() == 'Darwin':
            run_cmd(['brew', 'install', 'fzf'])
        else:
            raise Exception(f'Fzf not supported on {platform.system()}')
    return UdeFeature(
            name='fzf',
            envs={},
            post_install=None
            )

def setup_linux() -> None:
    run_cmd(['git','clone','--depth','1',
        'https://github.com/junegunn/fzf.git',
        '~/.fzf'])
    run_cmd(['~/.fzf/install'])

