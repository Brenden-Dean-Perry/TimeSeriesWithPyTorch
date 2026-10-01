from enum import Enum

class EnsemblingMethod(Enum):
    Averaging = 0,
    """
    Simple Averaging: For regression tasks, the ensemble averages the numerical outputs of all base models.	
    """
    Voting = 1,
    """
    Voting: For regression tasks, vote for the best numerical outputs of all base models. 
    For classification tasks, it uses majority voting (hard voting) or averages predicted probabilities 
    (soft voting) to pick the final class.	
    """
    WeightedAveraging = 2,
    """
    Weighted Averaging: Instead of treating every model equally, the ensemble assigns higher weights to more 
    accurate or reliable models, so their signals dominate the final prediction.
    """
    Bagging = 3,
    """
    Bagging (Bootstrap Aggregating): Trains multiple identical models in parallel on random subsets of the data 
    (with replacement) and aggregates their votes or averages to reduce variance and prevent overfitting.
    """
    Boosting = 4,
    """
    Boosting: Trains models sequentially where each new model focuses specifically on correcting the errors or 
    residuals left by the previous models, adjusting weights iteratively to reduce bias. 
    """
    Stacking = 5,
    """
    Stacking and Blending: Uses a secondary model (called a meta-model or blender) that takes the predictions of
    the base models as its input features and learns the optimal way to combine those signals into a final decision.
    """

