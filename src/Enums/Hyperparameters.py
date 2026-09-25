from enum import Enum


class Hyperparameters(Enum):
    LearningRateSchedule = 1,
    """
    A large LR will make good progress early but may overshoot as your model approaches a 
    minimum, while a rate small enough for fine-grained convergence may be painfully slow 
    at the start of training. LR schedulers dynamically adjust LR rate during training.
    The most practical scheduler for forecasting work is ReduceLROnPlateau, which monitors 
    a metric (typically validation loss) and reduces the LR when it stops improving.
    
    Our scheduler and early stopping work together, with the scheduler reducing LR to allow 
    finer convergence; if that still doesn’t help, early stopping terminates training. 
    Other common schedulers include cosine annealing, which smoothly decays LR following a 
    cosine curve, and step decay, which reduces LR by a fixed  factor at set intervals. 
    For most forecasting tasks, ReduceLROnPlateau is a practical starting point as it 
    adapts to your data rather than requiring you to guess when to reduce LR.
    """
    Epochs = 2
    """
    The number of times we pass an entire dataset through a neural network during training 
    (epoch) impacts its learning; by affecting the number of opportunities it has to learn 
    patterns from our dataset, which affects the overall accuracy of the model. 
    If we allow a model too few opportunities it can underfit, conversely too many 
    epochs may lead to overfitting which can be overcome with regularization and early 
    stopping, with the latter being especially important.
    """
    BatchSize = 3
    """
    Larger batch sizes generally lead to more accurate gradient approximations across a 
    dataset and more stable convergence, with a smoother optimization trajectory, but they 
    require more memory and can slow each training iteration.
    Smaller batch sizes allow more frequent parameter updates with less computational cost, 
    though the resulting gradient estimates are noisier. This noise can introduce more 
    variance into the learning process and a more erratic optimization path, which can help 
    optimizers escape shallow local minima.
    """
    Dropout = 4
    """
    Dropout is another regularization technique, which helps to prevent overfitting. 
    We simply provide a float value between 0 and 1 (e.g. 0.2 tells a network to drop 20% of 
    the nodes and their connections at each training iteration). This creates thinned network 
    architectures; applying this stochastic process promotes distributed and generalized 
    learning across a network, ensuring that no single neuron is solely responsible for 
    predicting specific features. Essentially, dropout breaks down complex co-adaptations among 
    neurons, forcing networks to learn more robust features, which in theory generalize better 
    to held-out data. It is implemented by multiplying neuron activations by a Bernoulli 
    random mask with keep probability 𝑝𝑝. During inference, dropout is not applied; instead, 
    neuron weights are scaled by 𝑝 to compensate for the increased number of active neurons 
    and prevent shifts in activation magnitudes.
    """
    BatchNormalization = 5
    """
    Batch normalization, which normalizes inputs to each layer to stabilize training. 
    Batch normalization normalizes the inputs to each layer during training, reducing 
    internal covariate shift, which is the change in the distribution of layer inputs 
    as weights are updated. By keeping these distributions more stable, batch normalization 
    allows higher learning rates and makes training less sensitive to weight initialization. 
    It also has a mild regularizing effect, similar to dropout, because the normalization 
    statistics computed on each mini-batch introduce noise.
    """
    WeightDecay = 6
    """
    Weight decay is a form of L2 regularization that penalizes large weights by adding a 
    fraction of the squared weight values to the loss function. This discourages a network 
    from relying too heavily on any single connection, which helps prevent overfitting, 
    particularly when we have limited training data.
    """