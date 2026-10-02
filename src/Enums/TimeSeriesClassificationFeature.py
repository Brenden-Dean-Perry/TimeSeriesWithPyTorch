from enum import Enum, auto


class TimeSeriesClassificationFeature(Enum):
    DistributionFeatures = auto(),
    """
    Shape, spread, skewness, kurtosis, central tendency, ect.
    """
    StationarityMeasures = auto()
    """
    Stationarity measures are measures of the degree to which a time series is stationary.
    """
    Autocorrelation = auto()
    """
    Autocorrelation measures the correlation between a time series and its lagged values.
    Detect temporal dependencies and cyclical patterns.
    """
    HighFluctions = auto()
    """
    Measures the portion of differences exceeding a threshold. Proxy for volatility.
    """
    ForecastingFeatures = auto()
    """
    Determines how predictive a time series is.
    Examples include forecasting error evaluating standard deviation of residules using 3 previous values to predict the next point.
    """
    EntropyFeatures = auto()
    """
    Quantify predictibility, regualrity, or complexity.
    High entropy indicates more complex and less predictable time series.
    Regularity (lower entropy suggest more predictable patterns. A chaotic system shows moderate entropy values.
    """
    FourierTransform = auto()
    """
    Fourier Transform is a mathematical tool for converting time series data into frequency domain
    unveiling periodic components as a collection of sinusoids functions.
    Informs Dominant frequencies, power distribution across frequencies, harmonic structures (related frequencies that form complex patterns)
    """
    DetrendedFluctuationAnalysis = auto()
    """
    detrended fluctuation analysis (DFA) unveils long-rang correlations and scaling properties in a series. 
    The main output is the scaling exponent which characterizes (1) correlation structure 
    (how fluctuations at different timescales relate to each other),
    (2) Persistence or anti-persistance: whether trends tend to continue (a>0.5) or reverse (a<0.5)
    (3) Fractal nature: If present, how self-similarity manifests across different scales.
    
    White noise: a = 0.5 (uncorrelated).
    
    Pink/1/f noise: a = 1 (long range correlations).
    
    Brownian motion: a = 1.5 (integrated white noise).
    """
    ComplexityFeatures = auto()
    """
    Complexity measures the complexity of a time series.
    Examples include:
    - Positive outlier timing
    - Negative outlier timing
    
    We can transform a series into a z-score and evaluate where the extreme values cluster within a series.
    Toward the beginning (output near -1), uniformly distributed values (output near 0), and toward the end (output near 1).
    
    """
    ShapeletBasedFeatures = auto()
    """
    Shapelet-based features are extracted from time series data using shapelets to identify local patterns.
    Similar to the idea of convolutional filters, shapelets are extracted from the time series data.
    The extracted shapelets rank series by distance and evaluate how well the ranking separates classes.
    A subset of shapelets are used to train a classifier with the maximum discriminative power.
    """
    DictionariesBasedFeatures = auto()
    """
    Dictionaries-based features are extracted from time series data using dictionaries to identify local patterns.
    For example, symbolic aggregate approximation (SAX) / bag-of-patterns (BoP)
    which discretizes the time series into a set of symbols/word representations to classify the time series.
    This method downsamples the time series and attempts to compress the data into symbolic representations.
    """