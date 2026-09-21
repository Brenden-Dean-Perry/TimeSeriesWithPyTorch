import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from typing import List


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

def plot_paired_autocorrelation_factors(df: pd.DataFrame, value_column: str, lags: int = 25,
                                color: str = 'blue', show: bool = True):
    # Facet plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    # ACF plot
    plot_acf(df[value_column], lags=lags, ax=ax1, color=color)
    ax1.set_title('Autocorrelation Function (ACF)')
    # PACF plot
    plot_pacf(df[value_column], lags=lags, ax=ax2, color=color)
    ax2.set_title('Partial Autocorrelation Function (PACF)')
    plt.tight_layout()

    if show:
        plt.show()

    return plt

def plot_seasonal_decompose(series, model='additive', figsize=(12, 10),
                            fontsize: int=14, custom_palette: List[str]=None):
    plt.rcParams.update({'font.size': fontsize})
    decomposition = seasonal_decompose(series, model=model)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=figsize, sharex=True)

    decomposition.observed.plot(ax=ax1, color=custom_palette[0], linewidth=0.5)
    ax1.set_ylabel('Observed', fontsize=fontsize)
    ax1.tick_params(axis='both', which='major', labelsize=fontsize-2)
    ax1.set_title('Observed Time Series', fontsize=fontsize)

    decomposition.trend.plot(ax=ax2, color=custom_palette[1], linewidth=1)
    ax2.set_ylabel('Trend', fontsize=fontsize)
    ax2.tick_params(axis='both', which='major', labelsize=fontsize-2)
    ax2.set_title('Trend Component', fontsize=fontsize)

    decomposition.seasonal.plot(ax=ax3, color=custom_palette[4], linewidth=0.5)
    ax3.set_ylabel('Seasonal', fontsize=fontsize)
    ax3.tick_params(axis='both', which='major', labelsize=fontsize-2)
    ax3.set_title('Seasonal Component', fontsize=fontsize)

    ax4.scatter(decomposition.resid.index, decomposition.resid, color=custom_palette[5], s=3, alpha=0.5)
    ax4.set_ylabel('Residual', fontsize=fontsize)
    ax4.set_xlabel('Date', fontsize=fontsize)
    ax4.tick_params(axis='both', which='major', labelsize=fontsize-2)
    ax4.set_title('Residual Component', fontsize=fontsize)

    plt.tight_layout()
    plt.subplots_adjust(top=0.95, hspace=0.3)
    return fig