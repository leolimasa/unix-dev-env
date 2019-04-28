from typing import Dict, List, Callable, Optional, Collection
from dataclasses import dataclass


@dataclass
class UdeFeature:
    name: str
    envs: Dict[str, str]
    post_install: Optional[Callable[['UdeEnvironment'], None]]


@dataclass
class UdeEnvironment:
    home_dir: str
    repo_dir: str
    ude_config_dir: str
    features: List[UdeFeature]
    systems: Collection[str]

    def enabled_features(self) -> List[str]:
        return [f.name for f in self.features]

