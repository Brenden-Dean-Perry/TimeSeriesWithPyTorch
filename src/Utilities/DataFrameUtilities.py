import pandas as pd


def dataframe_date_enrichment(df: pd.DataFrame, column_name: str = 'date') -> None:
    df[column_name] = pd.to_datetime(df[column_name])

    # Add additional features to data to help RF
    df['year'] = df[column_name].dt.year
    df['month'] = df[column_name].dt.month
    df['monthname'] = df[column_name].dt.strftime("%B")
    df['day'] = df[column_name].dt.day
    df['dayofweek'] = df[column_name].dt.dayofweek
    df['dayofweekname'] = df[column_name].dt.strftime('%A')
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)