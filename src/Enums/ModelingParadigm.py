from enum import Enum


class ModelingParadigm(Enum):
    """
    Modeling paradigms define the foundational approach and architectural philosophy used to represent, analyze, or
    predict data. When dealing with complex systems, data science and machine learning generally split these
    approaches into two competing or complementary paradigms: Global Modeling and Local Modeling.
    """
    LocalModeling = 1,
    """
    Develops multiple independent models, each tailored strictly to a specific sub-population, geographic region, 
    or single time series.
    """
    GlobalModeling = 2
    """
    Global modeling is an alternative paradigm, which forms the backbone of transfer learning. It allows us to build
     potentially more robust and efficient forecasting models. Fundamentally, Global Forecasting Models (GFMs) operate 
     on the premise that related series share some underlying structural patterns and data-generating processes (Joseph 
     and Tackes 2024, Ch. 15).
    """