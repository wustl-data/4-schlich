from typing import Callable, List

import pytest
import pandas as pd


@pytest.fixture
def salaries():
    return []


@pytest.fixture
def majors():
    return []


@pytest.fixture
def survey_factory() -> Callable:
    def lists_to_frame(salaries: List, majors: List) -> pd.DataFrame:
        return pd.DataFrame({"Salary": salaries, "Undergraduate Major": majors})

    return lists_to_frame


@pytest.fixture()
def survey(request) -> pd.DataFrame:
    salaries = request.param[1]
    majors = request.param[0]
    return pd.DataFrame(
        {
            "ConvertedComp": pd.Series(salaries, dtype="float64"),
            "UndergradMajor": pd.Series(majors, dtype="object"),
        }
    )


@pytest.fixture
def expected(request):
    majors = request.param[0]
    median_salaries = request.param[1]
    return pd.Series(
        median_salaries,
        index=pd.Index(majors, name="Undergraduate Major"),
        name="Median Salary",
    )
