from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd
import os


def setup(env: UdeEnvironment) -> UdeFeature:
    os.system("rustup update")
    os.system("cargo install cargo-edit")
    os.system("rustup component add rls rust-analysis rust-src")
    os.system('nvim "+CocInstall coc-rls" +qall')
    return UdeFeature(
        name="rust",
        envs={}
        )
