from dataclasses import dataclass


@dataclass(frozen=True)
class ModelSize:
    tiny: str = 'tiny'
    base: str = 'base'
    small: str = 'small'
    medium: str = 'medium'
    large: str = 'large'
