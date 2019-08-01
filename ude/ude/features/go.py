from ..fs import run_cmd, install_package
from ..model import UdeFeature, UdeEnvironment

def setup(env: UdeEnvironment) -> UdeFeature:
    run_cmd(['go', 'get', '-u', 'golang.org/x/tools/cmd/gopls'])
    return UdeFeature(
            name='go',
            envs={},
            post_install=None
    )
