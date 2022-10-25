import pandas as pd
import stacksurvey as so


import pandas as pd
import stacksurvey as so


def test_median_by_undergrad_no_data():
    # Arrange
    data = pd.DataFrame(
        {
            "NotTheSalaryColumn": [],
            "NotTheMajorColumn": [],
        }
    )

    # Act
    salaries = so.median_by_undergrad(data)

    # Assert
    assert salaries.name == "Salary"
    assert salaries.index.name == "Undergraduate Major"


def test_median_by_undergrad_single_major():
    data = pd.DataFrame(
        {
            "NotTheSalaryColumn": [1, 7, 9],
            "NotTheMajorColumn": ["A"] * 3,
        }
    )
    salaries = so.median_by_undergrad(data)
    pd.testing.assert_series_equal(
        salaries,
        pd.Series(
            [7.0],
            index=pd.Index(["A"], name="Undergraduate Major"),
            name="Salary",
        ),
    )


def test_quantiles():
    pass


def test_ecdf():
    pass


def test_gt_50_k():
    pass
