from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd


def setup(env: UdeEnvironment) -> UdeFeature:
    run_cmd(['npm', 'install', '-g', 'javascript-typescript-langserver'])
    run_cmd(['nvim', '"+CocInstall coc-tsserver"', '+qall'])
    return UdeFeature(
        name='typescript',
        envs={}
    )
