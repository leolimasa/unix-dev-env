from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, run_script
import platform
import os

def setup(env: UdeEnvironment) -> UdeFeature:
    return UdeFeature(
        name='csharp',
        envs={},
        post_install=None
    )
