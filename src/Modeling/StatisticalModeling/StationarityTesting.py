from statsmodels.tsa.stattools import kpss, adfuller


def kpss_stationarity_test(data: list):
    """
    Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test for stationarity.

    It is a robust test that is more powerful than ADF.
    Unlike the ADF, the KPSS test’s null hypothesis is that a time series is stationary.
    :param data:
    :return:
    """
    result = kpss(data)
    print('KPSS Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')

    for key, value in result[3].items():
        print('\t%s: %.3f' % (key, value))

def adfuller_stationarity_test(data: list):
    """
    Augmented Dickey-Fuller test for stationarity.
    The null hypothesis is that the data is non-stationary.

    ADF is a poor statistical test to rely on when you have high volatility,
    complex seasonal patterns, or exogenous variables.
    It fails to detect gradual trends when masked by high-frequency seasonal
    oscillations and volatility patterns.

    Use Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test for a more robust test.
    :param data:
    :return:
    """
    result = adfuller(data)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')

    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))