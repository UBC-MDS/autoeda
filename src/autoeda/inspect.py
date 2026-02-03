"""
Functions to support automated exploratory data analysis (EDA)
"""

import pandas as pd


def get_unary(df, target=None, threshold=0.75, dropna=False):
    """
    Returns a list of columns with a single value with a relative
    frequency percentage over a threshold (75% as default).
    In case user want only unary columns then threshold should be set to 1.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame to analyze.

    threshold : float, default=0.75
        Proportion threshold above which a column is considered unary.
        If set to 1.0, only columns with a single unique value
        are returned.

    dropna : bool, default=False
        Whether to exclude missing values (NaN) when computing value
        frequencies.

    Returns
    -------
    unary_cols : list of str
        List of column names identified as unary.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    unary_cols = []
    use_cols = [c for c in df if c != target]
    for col in use_cols:
        if df[col].nunique(dropna=dropna) == 0:
            continue

        max_freq = df[col].value_counts(normalize=True, dropna=dropna).iloc[0]

        if max_freq >= threshold:
            unary_cols.append(col)

    return unary_cols


def get_high_cardinality(df, max_unique_ratio=0.5):
    """
    Identify columns with high cardinality.

    A column is considered high cardinality if the ratio of unique values
    to the total number of rows exceeds `max_unique_ratio`.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame to inspect.
    max_unique_ratio : float, optional
        Maximum allowed ratio of unique values to total rows.
        Columns exceeding this threshold are flagged.
        Default is 0.5.

    Returns
    -------
    list of str
        List of column names with high cardinality.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    n_rows = len(df)
    if n_rows == 0:
        return []

    high_card_cols = [
        col
        for col in df.columns
        if df[col].nunique(dropna=True) / n_rows > max_unique_ratio
    ]

    return high_card_cols
