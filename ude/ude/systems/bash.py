import os
from ..model import UdeFeature, UdeEnvironment
from ..fs import run_cmd, rewrite_file_block, write_template


def setup(env: UdeEnvironment) -> None:
    bashrc_conf = os.path.join(env.ude_config_dir, "bashrc")
    rewrite_file_block("# UDE START\n", "# UDE END\n",
            os.path.join(env.home_dir, ".bash_profile"),
            f'source {bashrc_conf}\n')
    write_template("bashrc", env)
