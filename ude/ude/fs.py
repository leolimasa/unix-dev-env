from typing import List, Optional
import subprocess
import os
import re
import jinja2
from .model import UdeEnvironment


def run_cmd(command: List[str]) -> str:
    """
    Runs an OS command
    """
    return subprocess.check_output(command).decode('UTF-8')


def render_template(file_path: str, env: UdeEnvironment) -> str:
    """
    Finds file_name in the templates folder and outputs a rendered version
    passing the env to the template.
    """
    with open(file_path) as template_file:
        template = jinja2.Template(template_file.read())
        return template.render(env=env, enabled_features=env.enabled_features())

def write_template(template_file: str, env: UdeEnvironment, dest: Optional[str] = None):
    """
    Opens the template file, renders it with env, and saves it
    in the config dir.
    """
    final_dest = os.path.join(env.ude_config_dir, template_file) if dest is None else dest
    if not os.path.exists(os.path.dirname(final_dest)):
        os.makedirs(os.path.dirname(final_dest))
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    rendered = render_template(
        os.path.join(cur_dir, 'templates', template_file),
        env)
    write_to_file(final_dest, rendered)


def write_to_file(path: str, contents: str):
    file = open(path, 'w')
    file.write(contents)
    file.close()

def install_package(pkg: str):
    run_cmd(['brew', 'install', pkg])


def append_to_file(path: str, contents: str):
    """
    Appends a string to the file.
    """
    file = open(path, "a" if os.path.exists(path) else "w+")
    file.write(contents)
    file.close()

def create_file_if_not_exists(path: str):
    """
    Creates an empty file along with all directories if path
    does not exists.
    """
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    if not os.path.exists(path):
        with open(path, "w") as file:
            file.write("")


def rewrite_file_block(block_start: str, block_end: str, path: str, contents: str):
    """
    Rewrites the text between block_start and block_end with the contents string
    on the specified file.
    """
    create_file_if_not_exists(path)

    # Create regular expression pattern
    chop = re.compile(f'{block_start}.*?{block_end}', re.DOTALL)

    # Open file
    file = open(path, 'r')
    data = file.read()
    file.close()

    # Append or replace the contents
    new_block = f'{block_start}{contents}{block_end}'
    if data.find(block_start) == -1:
        data_edited = f'{data}\n{new_block}'
    else:
        data_edited = chop.sub(new_block, data)

    # Save result
    file = open(path, 'w')
    file.write(data_edited)
    file.close()
