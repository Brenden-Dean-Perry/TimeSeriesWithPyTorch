import pandas as pd


class FeatureEngineeringPipeline:
    """
    Feature Engineering Pipeline is a series of steps that are used to prepare the data for modeling.
    This pipeline is intended for automatic feature engineering & feature selection.
    """
    def __init__(self, df: pd.DataFrame, date_column: str):
        self.df = df
        self.date_column = date_column

    def run_pipeline(self):
        self.generate_feature_matrix()
        self.feature_evaluation_with_ols_regression()
        self.correlation_analysis()
        self.information_criterion_analysis()
        self.regularization_analysis()
        self.feature_importance_with_tree_based_models()
        self.granger_causality_analysis()

    def feature_evaluation_with_ols_regression(self):
        # R-squared, ect
        pass

    def granger_causality_analysis(self):
        pass

    def correlation_analysis(self):
        # spearman, pearson, ect
        pass

    def feature_importance_with_tree_based_models(self):
        # SHAP scoring, ect
        pass

    def information_criterion_analysis(self):
        # AIC, BIC, ect
        pass

    def generate_feature_matrix(self):
        pass

    def regularization_analysis(self):
        # L1, L2, ect
        pass