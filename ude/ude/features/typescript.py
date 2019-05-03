from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, run_script
import platform
import os

def setup(env: UdeEnvironment) -> UdeFeature:
    run_cmd(['npm', 'install', '-g', 'javascript-typescript-langserver'])
    return UdeFeature(
        name='typescript',
        envs={},
        post_install=None
    )

