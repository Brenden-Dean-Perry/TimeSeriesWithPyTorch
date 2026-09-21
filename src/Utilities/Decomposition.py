import pandas as pd
from statsmodels.tsa import seasonal as sm
from statsmodels.tsa.seasonal import seasonal_decompose


def generate_decomposition(df: pd.DataFrame, column: str):
    decomposition = sm.tsa.seasonal_decompose(df[column], period=28, model='additive')
    return decomposition.observed, decomposition.trend, decomposition.seasonal, decomposition.residule

def seasonal_decompose_series(series: pd.Series, model: str = 'additive'):
    return seasonal_decompose(series, model=model)