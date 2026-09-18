from enum import Enum


class SeriesModelingSteps(Enum):
    DataGathering = -1,
    DataPreparation = 0,
    DataImputation = 1,
    DataExploration = 2,
    FeatureEngineering = 3,
    Decomposition = 4,
    Modeling = 5,
    Forecast = 6,
    Validation = 7