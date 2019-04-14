from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, install_package

def setup(env: UdeEnvironment) -> UdeFeature:
    try:
        run_cmd(['which', 'fzf'])
    except:
        install_package('fzf')
    return UdeFeature(
            name='fzf',
            envs={}
            )

