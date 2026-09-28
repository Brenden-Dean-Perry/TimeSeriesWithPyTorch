from enum import Enum


class UncertaintyQuantificationMethod(Enum):
    Statistical = 1
    """
    Statistical Uncertainty Quantification relies on probability distributions to model 
    data and prediction uncertainties.
    
    Statistical methods (i.e. regression analysis, confidence intervals, and Monte
    Carlo simulations) strike a better balance between efficiency and accurate 
    uncertainty representation. Statistical approaches are more useful, but rely on 
    parametric assumptions and computationally intensive methods like Monte Carlo bootstrapping.
    """
    Bayesian = 2
    """
    Bayesian: Relies on prior knowledge about data to update beliefs about prediction 
    uncertainties.
    
    Bayesian statistics is useful when one has thoroughly investigated the data/topic to 
    be modeled, but its reliance on prior distributions is a problem for us when we are 
    modeling hundreds, or more, items. It is simply not practical to properly investigate 
    priors at scale, and not doing so often results in oversimplified or poorly selected 
    priors, and therefore poor UQ. 
    There is also the issue with Bayesian methods of being computationally expensive.
    """
    FuzzyLogic = 3
    """
    Fuzzy logic: Represents uncertainty using membership functions and fuzzy sets, 
    allowing partial set membership.
    
    Fuzzy logic simply lacks the precision needed for many business tasks, such as forecasting.
    """
    ConformalPrediction = 4
    """
    ConformalPrediction provide precise probabilistic intervals that are distribution-free, 
    model-agnostic, and generally computationally efficient (Manokhin and Sudjianto 2023).
    
    It is robust to imperfect and noisy data, making it suitable for real-world applications.
    It is non-parametric and distribution agnostic saving the need to investigate every 
    model’s data set fully. It provides probabilistic predictions with confidence metrics, 
    supporting informed decision-making. It produces valid prediction regions, enabling 
    rigorous uncertainty assessment (Angelopoulos and Bates 2023).
    """