from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd
import os
import platform


def setup(env: UdeEnvironment) -> UdeFeature:
    try:
        run_cmd(['which','rustc'])
    except:
        os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")
        os.system("rustup-init")
    os.system("rustup update")
    os.system("cargo install cargo-edit")
    os.system("rustup component add rls rust-analysis rust-src")
    return UdeFeature(
        name="rust",
        envs={},
        post_install=post_install
        ) 

def post_install(env: UdeEnvironment) -> None:
    os.system('nvim "+CocInstall coc-rls" +qall')
