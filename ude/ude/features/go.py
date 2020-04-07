from ..fs import run_cmd, install_package
from ..model import UdeFeature, UdeEnvironment
import os

def setup(env: UdeEnvironment) -> UdeFeature:

    # run_cmd(['go', 'get', 'golang.org/x/tools/cmd/gopls'], {'GO111MODULE': 'on'})
    os.system('GO111MODULE=on go get golang.org/x/tools/cmd/gopls@latest')

    return UdeFeature(
            name='go',
            envs={},
            post_install=None
    )
