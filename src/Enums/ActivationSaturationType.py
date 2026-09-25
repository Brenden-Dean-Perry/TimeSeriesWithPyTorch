from enum import Enum


class ActivationSaturationType(Enum):
    VanishingGradient = 1,
    ExplodingGradient = 2