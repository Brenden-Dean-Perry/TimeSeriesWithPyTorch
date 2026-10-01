from enum import Enum, auto


class SelfSupervisedContrastiveMethod(Enum):
    """Strategies for creating positive and negative pairs in time
    series contrastive learning."""
    AUGMENTATION = auto()
    """
    Creates views of the same underlying time series using transformations 
    (e.g., adding small random noise). Useful for both contrastive and 
    supervised learning data enhancement.
    """

    SAMPLING = auto()
    """
    Exploits temporal closeness; assumes adjacent segments are similar (positive pairs) 
    while randomly sampled segments are different (negative pairs).
    """

    PREDICTION = auto()
    """
    Contrasts representations in the latent space across time. Uses an autoregressive 
    model to predict future steps, treating actual future representations as positive 
    pairs and random steps as negative pairs.
    """

    PROTOTYPE = auto()
    """
    Contrasts representations against learnable cluster centroids (prototypes) 
    to capture global semantic structures and avoid false negatives.
    """

    EXPERT_KNOWLEDGE = auto()
    """
    Incorporates domain-specific heuristics or handcrafted features 
    (e.g., Fourier Transform, statistical properties) to guide pair selection.
    """