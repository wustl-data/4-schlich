import pytest
import pandas as pd


@pytest.fixture
def survey() -> pd.DataFrame:
    return lambda salaries, majors: pd.DataFrame(
        {"Salary": salaries, "Undergraduate Major": majors}
    )
