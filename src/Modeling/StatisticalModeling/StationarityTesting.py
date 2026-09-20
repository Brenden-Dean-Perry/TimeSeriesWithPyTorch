from statsmodels.tsa.stattools import kpss, adfuller


def kpss_stationarity_test(data: list):
    """
    Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test for stationarity.
    :param data:
    :return:
    """
    result = kpss(data)
    print('KPSS Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')

    for key, value in result[3].items():
        print('\t%s: %.3f' % (key, value))