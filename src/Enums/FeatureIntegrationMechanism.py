from enum import Enum


class FeatureIntegrationMechanism(Enum):
    """
    There are three primary approaches to combining global patterns with series-specific characteristics,
    each offering different advantages:
    """
    Concatenate = 1,
    """
    This is the most straightforward approach concatenates temporal features with series embeddings. 
    This can be effective for series with similar scales and patterns. 
    While computationally efficient, this approach assumes equal importance of global and series-specific features.
    """
    Attention = 2,
    """
    For more complex relationships, attention mechanisms can dynamically weight the importance of temporal features 
    based on series context. This makes it particularly useful for heterogeneous series with varying temporal 
    dependencies. We capture the weights in our attention layer, and apply them to the temporal features. 
    This mechanism allows the model to focus on relevant temporal patterns conditioned on series-specific context, 
    particularly valuable when series exhibit varying degrees of temporal dependence.
    """
    Gated = 3
    """
    Gating provides a learnable way to control the flow of information from both global and series-specific sources 
    through learned gates, which is useful when our series vary in their adherence to global patterns. It does 
    this by learning dimension-specific mixing coefficients through an activation function, in this case sigmoid,
    to control the balance between temporal and series-specific features. Unlike attention, which weights temporal 
    relationships, gating enables granular feature selection at each dimension; when a gate value approaches 1, 
    temporal features dominate, and when it approaches 0, series-specific characteristics prevail.
    """