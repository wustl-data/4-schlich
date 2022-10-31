import pandas as pd


def rename(survey_data):
    return survey_data.rename(
        columns={
            "UndergradMajor": "Undergraduate Major",
            "ConvertedComp": "Salary",
        }
    )
    

def median_by_undergrad(survey_data: pd.DataFrame) -> pd.Series:
    survey_data = rename(survey_data)
    return (
        survey_data.groupby("Undergraduate Major")["Salary"]
        .median()
        .rename("Median Salary")
    )
