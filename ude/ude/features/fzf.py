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
    fzf_path = path.join(env.home_dir, '.fzf')
    if not path.exists(fzf_path):
        run_cmd(['git', 'clone', '--depth', '1',
                 'https://github.com/junegunn/fzf.git',
                 fzf_path])
    run_cmd([path.join(fzf_path, 'install')])
