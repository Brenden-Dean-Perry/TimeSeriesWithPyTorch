from Enums.DecompositionType import DecompositionType


class DecompositionSeries:
    def __init__(self, decomposition_type: DecompositionType):
        self.observed : list = []
        self.trend : list = []
        self.seasonal : list = []
        self.cyclical : list = []
        self.exogenous_shocks : list = []
        self.residual : list = []
        self.decomposition_type : DecompositionType = decomposition_type
