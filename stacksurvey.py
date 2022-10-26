import pandas as pd


def median_by_undergrad(survey_data: pd.DataFrame) -> pd.Series:
    salaries = (
        survey_data.groupby("Major - Replace Me")["Salary - Replace Me"]
        .median()
        .rename("Median Salary")
    )
    salaries.index.name = "Undergraduate Major"
    return salaries
