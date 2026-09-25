from enum import Enum


class HyperparameterTuningMethod(Enum):
    """
    Hyperparameter Tuning Methods:
    While these are all decent approaches, metaheuristics tend to be more useful when
    we are conducting a large number of comparisons (Tani and Veelken, 2024). Grid search
    has its place too, especially when we want to create generalized but tailored
    default hyperparameters for large groups of data. However, the tried and tested way
    to find optimal hyperparameters for individual models is often Bayesian optimization
    (see Optuna package).
    """
    GridSearch = 1,
    """
    Grid Search - systematically creates and evaluates models for each combination of hyperparameter 
    values specified in a predefined grid. You can do a full grid search (slow!), 
    random search with a selected number of hyperparameters to compare, or more statistical 
    approaches like a Latin hypercube, which attempts to find a plausible set of values within 
    a multidimensional space. 
    """
    BayesianOptimization = 2,
    """
    Bayesian optimization models the performance as a function of hyperparameters using a 
    surrogate model, generally a Gaussian Process. It selects new hyperparameter values to 
    test, balancing exploration of new areas and exploitation of known good areas.
    """
    Metaheuristic = 3
    """
    Metaheuristics make use of heuristic algorithms to explore the search space. Some 
    common approaches include genetic algorithms, particle swarm optimization, and ant 
    colony optimization.
    """