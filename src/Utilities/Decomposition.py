import pandas as pd
from statsmodels.tsa import seasonal as sm


def test(df: pd.DataFrame, column: str):
    decomposition = sm.tsa.seasonal_decompose(df[column], period=28, model='additive')
    return decomposition.observed, decomposition.trend, decomposition.seasonal, decomposition.residule