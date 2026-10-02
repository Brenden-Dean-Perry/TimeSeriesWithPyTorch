from enum import Enum, auto


class TimeSeriesClusteringAlgorithm(Enum):
    """Categories of Time Series Clustering (TSCL) algorithms based on
    the taxonomy of Paparrizos, Yang, and Li (2024).
    """
    DISTANCE_BASED = auto()
    """
    Compute pairwise distances (e.g., using Dynamic Time Warping or other
    shape-aware measures) and apply traditional clustering algorithms like
    k-means or hierarchical clustering.
    """
    DISTRIBUTION_BASED = auto()
    """
    Fit probabilistic or statistical models and cluster in parameter or density space.
    """

    FEATURE_BASED = auto()
    """
    Transform time series into fixed-length vectors of descriptive statistics,
    enabling the use of standard clustering techniques.
    """

    REPRESENTATION_LEARNING = auto()
    """
    Use neural networks to learn latent embeddings that capture temporal patterns,
    though these models are black boxes with less interpretability.
    """