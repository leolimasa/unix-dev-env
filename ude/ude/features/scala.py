from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, install_package
import os
import platform


def setup(env: UdeEnvironment) -> UdeFeature:
    try:
        run_cmd(['which', 'metals-vim'])
    except:
        os.system('curl -L -o coursier https://git.io/coursier')
        os.system('chmod +x coursier')
        os.system(('./coursier bootstrap '
                   '--java-opt -Xss4m '
                   '--java-opt -Xms100m '
                   '--java-opt -Dmetals.client=coc.nvim '
                   'org.scalameta:metals_2.12:0.7.0 '
                   '-r bintray:scalacenter/releases '
                   '-r sonatype:snapshots '
                   '-o /usr/local/bin/metals-vim -f'
                   ))
    return UdeFeature(
        name='scala',
        envs={},
        post_install=None
    )
