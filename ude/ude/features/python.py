from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd


def setup(env: UdeEnvironment) -> UdeFeature:
    run_cmd(['pip3', 'install', 'python-language-server[all]'])
    run_cmd(['pip3', 'install', 'pynvim'])
    return UdeFeature(
        name='python',
        envs={},
        post_install=post_install
    )

def post_install(env: UdeEnvironment) -> None:
    if 'neovim' in env.systems:
        run_cmd(['nvim', '"+CocInstall coc-python"', '+qall'])
