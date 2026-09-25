from enum import Enum



class DataSplittingTechnique(Enum):
    """
    Data Splitting Techniques - Techniques for splitting the data.
    """
    TrainingValidationTestSplit = 1,
    """
    When establishing hyperparameters for neural networks, we use a fixed 
    training-validation-test split rather than nested cross-validation. 
    Instead of splitting training and validation into multiple folds, 
    we reuse the same split for each hyperparameter set. 
    This is more robust than a simple training-test split for hyperparameter tuning 
    while being computationally feasible. For example, with a time series of 730 periods 
    (2 years of daily data) and a forecast horizon of 90 periods, we might split our data 
    into approximately 550-90-90, with the training set comprising approximately 75% of our data.
    """
    TrainingValidationSplit = 2,
    """
    After identifying your architecture, optimizer, and hyperparameters, you train a model on 
    a larger portion of the data using a training-validation split. There is no separate test 
    set here because hyperparameter selection is already complete. The validation set provides 
    a final performance metric on unseen data that can be compared against the tuning stage.
    """
    FullDatasetTrainingAndFineTuning = 3
    """
    we can fine-tune; rather than rebuilding from scratch, we take an already-trained model 
    and continue training it on new or additional data (e.g. recent pricing or sales data). 
    This allows us to update our model with all available data without starting over. 
    While fine-tuning is a useful approach, especially if our data is stable, our models 
    can drift out of sync with the data they are modeling. It is wise to monitor performance 
    carefully when applying this approach over time.
    """