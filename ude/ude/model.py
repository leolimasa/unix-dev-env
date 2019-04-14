from typing import Dict, List
from dataclasses import dataclass


@dataclass
class UdeFeature:
    name: str
    envs: Dict[str, str]


@dataclass
class UdeEnvironment:
    home_dir: str
    repo_dir: str
    ude_config_dir: str
    features: List[UdeFeature]

    def enabled_features(self) -> List[str]:
        return [f.name for f in self.features]

