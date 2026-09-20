import pandas as pd
from typing import List, Union


def dataframe_set_index(df: pd.DataFrame, column_name: str):
    """
    Sets the given column as the index of the dataframe.
    :param df:
    :param column_name:
    :return:
    """
    if df.index.name != column_name:
        df.set_index(column_name, inplace=True)

def dataframe_set_datatype_as_date(df: pd.DataFrame, columns: Union[str,List[str]]):
    """
    Sets the date type of the given columns as dates in the dataframe.
    :param df:
    :param columns:
    :return:
    """
    if isinstance(columns, str):
        if df.index.name != columns:
            df[columns] = pd.to_datetime(df[columns])
    else :
        for column_name in columns:
            if df.index.name != columns:
                df[column_name] = pd.to_datetime(df[column_name])

def dataframe_date_enrichment(df: pd.DataFrame, column_name: str = 'date') -> None:
    """
    Enriches the given dataframe with additional date features.
    :param df:
    :param column_name:
    :return:
    """
    dataframe_set_datatype_as_date(df, column_name)

    # Add additional features to data to help RF
    df['year'] = df[column_name].dt.year
    df['month'] = df[column_name].dt.month
    df['monthname'] = df[column_name].dt.strftime("%B")
    df['day'] = df[column_name].dt.day
    df['dayofweek'] = df[column_name].dt.dayofweek
    df['dayofweekname'] = df[column_name].dt.strftime('%A')
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)