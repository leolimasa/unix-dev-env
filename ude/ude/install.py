from typing import List, Callable, Dict
from dataclasses import replace
from functools import reduce
import os
import pathlib
from .systems import neovim
from .features import python
from .model import UdeEnvironment, UdeFeature

FeatureSetup = Callable[[UdeEnvironment], UdeFeature]
SystemSetup = Callable[[UdeEnvironment], None]

all_features: Dict[str, FeatureSetup] = {
    'python': python.setup
}

all_systems: Dict[str, SystemSetup] = {
    'neovim': neovim.setup
}


def setup_feature(feature: FeatureSetup, env: UdeEnvironment) -> UdeEnvironment:
    """
    Run the feature setup for the specified feature in the systems list.
    """
    new_feature = feature(env)
    return replace(env, features=env.features + [new_feature])


def setup_features(feature_list: Dict[str, FeatureSetup], features: List[str], env: UdeEnvironment) -> UdeEnvironment:
    """
    Sets up all features specified in the features argument.
    Setup must be included in feature_list.
    """
    return reduce(
        lambda env, feature: setup_feature(feature_list[feature], env),
        features,
        env)


def setup_systems(systems_list: Dict[str, SystemSetup], systems: List[str], env: UdeEnvironment):
    """
    Run the system setup for the specified system in the systems list.
    """
    for system in systems:
        systems_list[system](env)


def setup(feature_list: Dict[str, FeatureSetup],
          systems_list: Dict[str, SystemSetup],
          features: List[str],
          systems: List[str],
          env: UdeEnvironment):
    """
    Sets up all systems and features specified in the lists.
    """
    new_env = setup_features(feature_list, features, env)
    setup_systems(systems_list, systems, new_env)


def split_and_trim(input: str) -> List[str]:
    splat = input.split(',')
    return [item.strip() for item in splat]

def env_is_set(env: str):
    return os.getenv(env, False) != False

def main():
    home = os.getenv('UDE_USER_HOME', str(pathlib.Path.home()))
    ude_config_dir = os.getenv(
        'UDE_CONFIG_DIR', os.path.join(home, '.config', 'ude'))
    os.makedirs(ude_config_dir)
    features = (split_and_trim(os.getenv('UDE_FEATURES', '')) 
        if env_is_set('UDE_FEATURES') else all_features.values())
    systems = (split_and_trim(os.getenv('UDE_SYSTEMS', ''))
        if env_is_set('UDE_SYSTEMS') else all_systems.values())
    env = UdeEnvironment(
        home_dir=home,
        ude_config_dir=ude_config_dir,
        features=[]
    )
    setup(all_features, all_systems, features, systems, env)


if __name__ == "__main__":
    main()

