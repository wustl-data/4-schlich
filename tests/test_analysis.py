import pandas as pd
import stacksurvey as so
import pytest


@pytest.mark.parametrize(
    "survey, expected",
    [
        ([[], []], [[], []]),
        (
            [["CompSci"] * 3, [30000, 70000, 90000]],
            [["CompSci"], [70000.0]],
        ),
    ],
    indirect=True,
)
def test_median_by_undergrad_no_data(survey, expected):

    # Act
    salaries = so.median_by_undergrad(survey)

    # Assert
    pd.testing.assert_series_equal(salaries, expected)


def test_quantiles():
    pass


def test_ecdf():
    pass


def test_gt_50_k():
    pass
