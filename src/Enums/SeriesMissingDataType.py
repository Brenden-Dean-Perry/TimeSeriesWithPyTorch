from enum import Enum

# enum
class SeriesMissingDataType(Enum):

    MissingAtRandom = 1,
    """
    Missing at random indicates that the data is missing at random
    (i.e. missing with probability p or because data observations are irregular.)
    """

    NotMissingAtRandom = 2
    """
    Not missing at random indicates that the data is missing on a 
    regular basis possible do to structural reasons.
    """