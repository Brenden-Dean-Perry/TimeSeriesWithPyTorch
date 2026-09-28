from enum import Enum


class UncertaintyQuantificationSource(Enum):
    """
    Uncertainty Quantification Sources - Types of uncertainty quantification sources.
    Two main sources of uncertainty are aleatoric and epistemic.
    """
    Aleatoric = 1
    """
    Aleatoric caused by intrinsic randomness
    and variability within data, as a feature of the systems we investigate, i.e., stock market prices"""
    Epistemic = 2
    """
    Epistemic uncertainty originates from incomplete knowledge/understanding.
    """