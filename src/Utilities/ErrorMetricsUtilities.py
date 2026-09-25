import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
import pandas as pd

def mae(actual, predicted):
    return np.mean(np.abs(predicted - actual))

def mse(actual, predicted):
    return np.mean(np.square(predicted - actual))

def rmse(actual, predicted):
    return np.sqrt(np.mean(np.square(predicted - actual)))

def mape(actual, predicted):
    mask = actual != 0
    return np.mean(np.abs((actual[mask] - predicted[mask]) / actual[mask])) * 100

def smape(actual, predicted):
    return 100 / len(actual) * np.sum(
        2 * np.abs(predicted - actual) / (np.abs(actual) + np.abs(predicted)))

def calculate_metrics(actual, forecast):
    mae = mean_absolute_error(actual, forecast)
    rmse = np.sqrt(mean_squared_error(actual, forecast))
    mape = mean_absolute_percentage_error(actual+1, np.array(forecast)+1)
    return mae, rmse, mape

def calculate_metrics_table(unscaled_actuals,):
    errors = {'Activation': [], 'MAE': [], 'MSE': [], 'RMSE': [], 'MAPE': [], 'sMAPE': []}
    for name, preds in results.items():
        errors['Activation'].append(name)
        errors['MAE'].append(mean_absolute_error(unscaled_actuals, preds))
        errors['MSE'].append(mean_squared_error(unscaled_actuals, preds))
        errors['RMSE'].append(rmse(unscaled_actuals, preds))
        errors['MAPE'].append(mape(unscaled_actuals, preds))
        errors['sMAPE'].append(smape(unscaled_actuals, preds))
    print(pd.DataFrame(errors).to_string(index=False))

def calculate_scaled_metrics(actual, forecast, training_data):
    in_sample_mae = np.mean(np.abs(np.diff(training_data)))
    if in_sample_mae == 0:
        return np.inf, np.inf
    errors = np.abs(actual - forecast)
    squared_errors = (actual - forecast) ** 2
    mase = np.mean(errors) / in_sample_mae
    rmsse = np.sqrt(np.mean(squared_errors)) / in_sample_mae
    return mase, rmsse

def calculate_relative_errors(actual, forecast, baseline_metrics):
    mae, rmse, mape = calculate_metrics(actual, forecast)
    rel_mae = (mae / baseline_metrics[0] if baseline_metrics[0] != 0 else np.inf)
    rel_rmse = (rmse / baseline_metrics[1] if baseline_metrics[1] != 0 else np.inf)
    rel_mape = (mape / baseline_metrics[2] if baseline_metrics[2] != 0 else np.inf)
    return rel_mae, rel_rmse, rel_mape