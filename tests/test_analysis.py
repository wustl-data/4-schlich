import pandas as pd
import stacksurvey as so


def test_median_by_undergrad_no_data():
    # Arrange
    data = pd.DataFrame(
        {
            "Salary - Replace Me": [],
            "Major - Replace Me": [],
        }
    )

    # Act
    salaries = so.median_by_undergrad(data)

    # Assert
    assert salaries.name == "Median Salary"
    assert salaries.index.name == "Undergraduate Major"


def test_median_by_undergrad_single_major():
    data = pd.DataFrame(
        {
            "Salary - Replace Me": [30000, 70000, 90000],
            "Major - Replace Me": ["CompSci"] * 3,
        }
    )
    salaries = so.median_by_undergrad(data)
    pd.testing.assert_series_equal(
        salaries,
        pd.Series(
            [70000.0],
            index=pd.Index(["CompSci"], name="Undergraduate Major"),
            name="Median Salary",
        ),
    )


def test_quantiles():
    pass


def test_ecdf():
    pass


def test_gt_50_k():
    pass
