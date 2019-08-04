from ..fs import run_cmd, install_package, write_template
from ..model import UdeFeature, UdeEnvironment
from os import path

def setup(env: UdeEnvironment) -> UdeFeature:
    return UdeFeature(
            name='transparent_theme',
            envs={},
            post_install=post_install
    )

def post_install(env: UdeEnvironment) -> None:
    if not "neovim" in env.systems:
        return
    nvim_path =  path.join(env.home_dir, ".config", "nvim")
    theme_path = path.join(nvim_path, "colors", "transparent-theme.vim")
    airline_themes_path = path.join(nvim_path, "autoload", "airline", "themes", "transparentairlinetheme.vim")
    write_template("transparent-theme.vim", env, theme_path)
    write_template("transparentairlinetheme.vim", env, airline_themes_path)


