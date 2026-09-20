import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def plot_timeseries(df : pd.DataFrame, x_column : str, y_column : str, title : str = None,
                    x_label : str = None, y_label : str = None,
                    color : str = 'blue', marker : str = None, show : bool = True):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df[x_column], df[y_column], color=color, marker=None if marker is None else marker)
    ax.set_xlabel(x_column.title() if x_label is None else x_label)
    ax.set_ylabel(y_column.title() if y_label is None else y_label)
    ax.set_title(title)
    plt.rcParams['font.size'] = 16
    plt.tight_layout()

    if show:
        plt.show()

    return plt, fig, ax

def plot_boxplot_single(df : pd.DataFrame, column : str, title : str = None, show : bool = True):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.boxplot(df[column])
    ax.set_title(title)
    plt.tight_layout()

    if show:
        plt.show()

    return plt, fig, ax

def plot_boxplot(df : pd.DataFrame, value_column : str, grouping_column: str, title : str = None,
            value_column_label : str = None, grouping_column_label : str = None,
             show_outliers: bool = True, horizontal : bool = False, custom_palette : list = None,
                 show : bool = True):
    sns.boxplot(
        x=value_column, y=grouping_column, hue=grouping_column,
        data=df,
        palette=custom_palette, showfliers=show_outliers, legend=False, orient="h" if horizontal else "v"
    )
    plt.xlabel(value_column.title() if value_column_label is None else value_column_label, fontsize=18)
    plt.ylabel(grouping_column.title() if grouping_column_label is None else grouping_column_label, fontsize=18)
    plt.title(title, fontsize=20)

    if show:
        plt.show()

    return plt

def plot_autocorrelation_factor(df: pd.DataFrame, value_column: str, lags: int = 25,
                                color: str = 'blue', show: bool = True):
    plot_acf(df[value_column], lags=lags, color=color)
    plt.xlabel('Lag/Shift', fontsize=14)
    plt.ylabel('Correlation Coefficient', fontsize=14)
    plt.tight_layout()

    if show:
        plt.show()

    return plt

def plot_partial_autocorrelation_factor(df: pd.DataFrame, value_column: str, lags: int = 25,
                                color: str = 'blue', show: bool = True):
    plot_pacf(df[value_column], lags=lags, color=color)
    plt.xlabel('Lag/Shift', fontsize=14)
    plt.ylabel('Correlation Coefficient', fontsize=14)
    plt.tight_layout()

    if show:
        plt.show()

    return plt