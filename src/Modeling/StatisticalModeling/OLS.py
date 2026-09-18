import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


def ols_model_summary(x : np.array, y : np.array):
    """
    OLS linear regression model statistical summary.
    :param x:
    :param y:
    :return:
    """
    # 1. Manually add an intercept (constant column) to X
    X_with_constant = sm.add_constant(x)

    # 2. Instantiate and fit the model (Note: y comes first)
    model = sm.OLS(y, X_with_constant).fit()

    # 3. Print the comprehensive statistics report
    print(model.summary())

def ols_model(x : np.array, y : np.array):
    # 1. Instantiate and fit the model
    model = LinearRegression()
    model.fit(x, y)

    # 2. Extract key metrics
    print(f"Intercept (b0): {model.intercept_}")
    print(f"Slope Coefficient (b1): {model.coef_[0]}")
    print(f"R-squared: {model.score(X, y)}")

    # 3. Predict new values
    predictions = model.predict(np.array([[6]]))
    print(f"Prediction for X=6: {predictions[0]}")