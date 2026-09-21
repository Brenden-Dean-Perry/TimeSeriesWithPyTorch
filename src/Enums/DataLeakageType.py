from enum import Enum


class DataLeakageType(Enum):
    """
    Data Leakage Types - Types of data leakage that can occur.
    """

    Transformation = 1,
    """
    Transformation Data Leakage is when leakage is caused by a transformation.
    """

    LookForwardBias = 2,
    """
    Look forward Bias Data Leakage is when leakage is caused by the inclusion of 
    strongly correlated variables that we are trying to predict.
    """

    PanelLeakage = 3
    """
    Panel Data Leakage is when leakage is caused by the inclusion of correlated covariants in cross-sectional data.
    """
