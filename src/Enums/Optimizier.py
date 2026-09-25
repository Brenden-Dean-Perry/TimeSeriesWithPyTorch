from enum import Enum


class Optimizier(Enum):
    SGD = 1
    """
    Stochastic Gradient Descent uses individual samples to update parameters, which is faster 
    than GD. But because the model is updated after every single sample, this high variance 
    causes large fluctuations in the objective function during training. This can be 
    advantageous for escaping local minima, but can also lead to getting trapped in one. 
    We can tune the learning rate to reduce oscillations in the objective.
    """
    GD = 2
    """
    Gradient descent uses an entire dataset to perform parameter updates, making
    it computationally expensive.
    """
    MGD = 4
    """
    MGD computes gradients on small batches of data, resulting in less variation of the 
    objective function compared to SGD. It is generally preferred over other gradient 
    descent methods because of its balance between efficiency and convergence stability.
    """
    Adam = 5
    """
    Adam combines the advantages of Adadelta/RMSprop and momentum. It is currently the 
    default optimizer for most forecasting libraries utilizing neural networks. Its 
    advantage is that it works well with sparse data due to its adaptive learning rates, 
    without requiring manual tuning of the global learning rate.
    """
    Adadelta = 6
    """
    Adadelta improves on Adagrad by using a fixed window of past gradients to avoid 
    vanishing learning rates.
    """
    RMSprop = 7
    """
    RMSprop is similar to Adadelta but uses a different approach to managing past 
    gradients. It adjusts learning rates for each parameter dynamically, dividing the 
    learning rate by a running average of the magnitudes of recent gradients for that weight.
    """
    Adagrad = 8
    """
    Adagrad adapts learning rates, with smaller updates for frequent features and larger 
    updates for rarer ones. While this allows the optimizer to capture information from 
    rarer features, it can result in vanishing learning rates, where the rate becomes too 
    small too early in training.
    """