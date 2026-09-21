from enum import Enum


class TimeSeriesCrossValidationType(Enum):
    KFold = 1,
    """
    K-Fold Cross Validation - K-Fold cross validation is a method of splitting a dataset into K equal parts.
    One fold is used as a validation set, and the K-1 remaining folds are used as training sets.
    """
    KFoldExpandingWindow = 2
    """
    K-Fold Expanding Window Cross Validation - K-Fold expanding window cross validation is a method of splitting a dataset into K equal parts.
    One fold is used as a validation set, and the K-1 remaining folds are used as training sets. 
    The training sets are expanded as the validation set is moved forward."""
    KFoldRollingWindow = 3
    """
    K-Fold Rolling Window Cross Validation - K-Fold rolling window cross validation is a method of splitting a dataset into K equal parts.
    One fold is used as a validation set, and the K-1 remaining folds are used as training sets. 
    The training sets are rolled as the validation set is moved forward."""