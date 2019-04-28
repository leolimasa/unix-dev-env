from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd


def setup(env: UdeEnvironment) -> UdeFeature:
    run_cmd(['npm', 'install', '-g', 'javascript-typescript-langserver'])
    return UdeFeature(
        name='typescript',
        envs={},
        post_install=post_install
    )

def post_install(env: UdeEnvironment) -> None:
    run_cmd(['nvim', '"+CocInstall coc-tsserver"', '+qall'])
