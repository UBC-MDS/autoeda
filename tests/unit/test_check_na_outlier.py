import pandas as pd
import pytest

from autoeda.check_na_outlier import check_na_outliers


def test_basic_summary_structure():
    """
    Check that the function should return a DataFrame summary,
    with one row per column in the input DataFrame. The dataframe
    include NA and outlier statistics
    """
    df = pd.DataFrame(
        {
            "num": [1, 2, 3, 100],
            "cat": ["a", "b", None, "c"],
        }
    )

    result = check_na_outliers(df)

    assert isinstance(result, pd.DataFrame)
    assert result.shape[0] == 2
    assert "na_count" in result.columns
    assert "outlier_count" in result.columns


def test_non_numeric_column_outlier_not_applicable():
    """
    Check that outlier statistics should only apply to numeric columns.
    Non-numeric columns should be ignored and not cause errors
    """
    df = pd.DataFrame({"cat": ["a", "b", "c", None]})

    result = check_na_outliers(df)

    assert pd.isna(result.loc[0, "outlier_count"])
    assert pd.isna(result.loc[0, "outlier_proportion"])


def test_na_risk_high_when_exceeds_threshold():
    """
    Check that columns with NA proportion above na_threshold
    should be flagged as high risk
    """
    df = pd.DataFrame({"x": [1, None, None, None]})

    result = check_na_outliers(df, na_threshold=0.5)

    assert result.loc[0, "na_risk"] == "high"


def test_outlier_risk_low_for_numeric_column():
    """
    Check that Numeric columns with not many outliers
    should be flagged as low risk
    """
    df = pd.DataFrame({"x": [1, 1, 1, 1, 100]})

    result = check_na_outliers(df, outlier_method="iqr", outlier_threshold=0.1)

    assert result.loc[0, "outlier_risk"] == "low"


def test_outlier_risk_high_when_many_outliers():
    """
    Numeric columns with a high proportion of outliers
    should be flagged as high risk.
    """
    df = pd.DataFrame({"x": [1, 2, 3, 5, 100, 100, 100]})

    result = check_na_outliers(df, outlier_method="mad", outlier_threshold=0.1)

    assert result.loc[0, "outlier_risk"] == "high"


def test_return_risk_false_removes_risk_columns():
    """
    If return_risk is False, risk columns
    should not be included in the output
    """
    df = pd.DataFrame({"x": [1, 2, 3]})

    result = check_na_outliers(df, return_risk=False)

    assert "na_risk" not in result.columns
    assert "outlier_risk" not in result.columns


def test_invalid_df_type_raises_error():
    """
    Check that the function should raise error when the input df
    is not a pandas DataFrame
    """
    with pytest.raises(TypeError):
        check_na_outliers([1, 2, 3])


def test_invalid_outlier_method_raises_error():
    """
    check that the function raise error when outlier_method
    is not one of {'auto', 'iqr', 'zscore', 'mad'}
    """
    df = pd.DataFrame({"x": [1, 2, 3]})

    with pytest.raises(ValueError):
        check_na_outliers(df, outlier_method="invalid")
