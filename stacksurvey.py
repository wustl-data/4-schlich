import pandas as pd


def median_by_undergrad(survey_data: pd.DataFrame) -> pd.Series:
    return survey_data.groupby("Major")["Salary"].median()
