from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd


def setup(env: UdeEnvironment) -> UdeFeature:
    run_cmd(['pip3', 'install', 'python-language-server[all]'])
    run_cmd(['pip3', 'install', 'pynvim'])
    return UdeFeature(
        name='python',
        envs={}
    )
