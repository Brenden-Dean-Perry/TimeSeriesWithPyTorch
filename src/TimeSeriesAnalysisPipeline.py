import pandas as pd
from TimeSeriesAnalysisResult import TimeSeriesAnalysisResult


class TimeSeriesAnalysisPipeline:
    def __init__(self, df: pd.DataFrame, date_column: str):
        self.df: pd.DataFrame = df
        self.date_column: str = date_column

    def run_pipeline(self) -> TimeSeriesAnalysisResult:
        result = TimeSeriesAnalysisResult()
        self.dataframe_enrichment()
        self.data_imputation()
        self.data_exploration_analysis()
        self.vizualization()
        self.transform_data()
        self.stationarity_analysis()
        self.variation_analysis()
        self.trend_analysis()
        self.seasonality_analysis()
        self.cyclical_analysis()
        self.autocorrelation_analysis()
        self.partial_autocorrelation_analysis()
        self.exogenous_shocks_analysis()
        self.residual_analysis()
        self.full_decomposition_analysis()
        self.cointegration_analysis()
        self.causal_analysis()
        self.generate_naive_models()
        self.error_measurement()
        self.scoring_analysis()

        return result

    def dataframe_enrichment(self):
        pass

    def data_imputation(self):
        pass

    def data_exploration_analysis(self):
        pass

    def variation_analysis(self):
        # heteroskedasticity
        pass

    def trend_analysis(self):
        pass

    def seasonality_analysis(self):
        pass

    def cyclical_analysis(self):
        pass

    def exogenous_shocks_analysis(self):
        # exogenous variables / covariates
        pass

    def residual_analysis(self):
        # tests for independence, normality, homoskedasticity.
        # residuals should be normally distributed and should not be correlated with each other.
        # Should be homoscedastity
        # there should be no autocorrelation in residuals.
        pass

    def full_decomposition_analysis(self):
        pass

    def stationarity_analysis(self):
        pass

    def autocorrelation_analysis(self):
        pass

    def partial_autocorrelation_analysis(self):
        pass

    def normality_analysis(self):
        # QQ-plot, ect
        pass

    def generate_naive_models(self):
        # Standard naive / seasonal nieve / naie with drift
        # these can be used to compare more advanced models against niave benchmarks.
        pass

    def error_measurement(self):
        pass

    def cointegration_analysis(self):
        pass

    def causal_analysis(self):
        pass

    def vizualization(self):
        pass

    def scoring_analysis(self):
        # brier score, r^2 of model forecasts against out if of sample data.
        pass

    def transform_data(self):
        pass

    def stationarity_transform(self):
        # detrend, differencing, log, power transform, ect
        pass