from enum import Enum, auto


class SelfSupervisedLearningMethod(Enum):
    """
    In a review work, Self-Supervised Learning for Time Series Analysis:
    Taxonomy, Progress, and Prospects, Kexin Zhang and
    colleagues categorize self-supervised learning into three main categories:
    generative methods, contrastive methods, and adversarial methods.
    """
    Generative = auto()
    """
    Generative methods (e.g., autoencoders) rely on reconstructing the input data. 
    Because reconstruction is a low-level and local task, the model excels at 
    capturing local structures. However, missing high-level and global structures 
    can hinder performance on tasks like time series classification.
    """

    Contrastive = auto()
    """
    Contrastive methods compare different segments or views of time series data. 
    They evaluate representations of known pairs to bring positive pairs (similar 
    views) closer together and push negative pairs (different or augmented views, 
    such as reversed/flipped series) apart in the embedding space.
    """

    Adversarial = auto()
    """
    Adversarial methods utilize an adversarial framework (typically a generator 
    and a discriminator) to learn robust data representations by optimizing 
    against a competing objective.
    """