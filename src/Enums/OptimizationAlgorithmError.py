from enum import Enum


class OptimizationAlgorithmError(Enum):
    LocalMinima = 1,
    SaddlePoint = 2,
    VanishingGradient = 3