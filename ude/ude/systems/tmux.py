import os
from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, rewrite_file_block, write_template


def setup(env: UdeEnvironment) -> None:
    tmux_conf = os.path.join(env.ude_config_dir, "tmux.conf")
    rewrite_file_block("# UDE START\n", "# UDE END\n",
            os.path.join(env.home_dir, ".tmux.conf"),
            f'source-file {tmux_conf}\n')
    write_template("tmux.conf", env)
