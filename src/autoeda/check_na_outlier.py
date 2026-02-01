"""
Functions to support automated exploratory data analysis (EDA)
"""

import numpy as np
import pandas as pd


def check_na_outliers(
    df,
    outlier_method="auto",
    na_threshold=0.1,
    outlier_threshold=0.05,
    return_risk=True,
    return_suggestions=True,
):
    """
    Diagnose missing values and outliers in a DataFrame.

    This function summarizes the amount of missing values
    and potential outliers for each column in the input dataset.
    It is intended for exploratory data analysis and provides
    interpretable diagnostics for future data preprocessing.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset for exploratory data analysis.
    outlier_method : {"auto", "iqr", "zscore", "mad"}, default="auto"
        Method used to detect outliers in numeric columns. If "auto",
        the most appropriate method is selected,
        based on the distribution of each column.
    na_threshold : float, default=0.1
        Proportion threshold above which missing values are flagged
        as high risk. Further investigation or imputation may be needed
        if there are lots of missing values.
    outlier_threshold : float, default=0.05
        Proportion threshold above which outliers are flagged
        as high risk.
    return_risk : bool, default=True
        Whether to compute and return qualitative risk levels
        (e.g., "low", "medium", "high") based on the specified
        thresholds.
    return_suggestions : bool, default=True
        Whether to include suggested actions for handling missing
        values and outliers (e.g., imputation or transformation).

    Returns
    -------
    pandas.DataFrame
        A summary table with one row per column, including
        missing value statistics, outlier statistics (for numeric
        columns), and optional risk levels and suggested actions.
    """

    # Input validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")

    if not 0 <= na_threshold <= 1:
        raise ValueError("na_threshold must be between 0 and 1.")

    if not 0 <= outlier_threshold <= 1:
        raise ValueError("outlier_threshold must be between 0 and 1.")

    valid_methods = {"auto", "iqr", "zscore", "mad"}
    if outlier_method not in valid_methods:
        raise ValueError(f"outlier_method must be one of {valid_methods}.")

    results = []

    # Helper functions to detect outliers
    def detect_outliers_iqr(x):
        q1, q3 = np.percentile(x, [25, 75])
        iqr = q3 - q1
        if iqr == 0:
            return np.zeros_like(x, dtype=bool)
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return (x < lower) | (x > upper)

    def detect_outliers_zscore(x):
        mean = np.mean(x)
        std = np.std(x, ddof=0)
        if std == 0:
            return np.zeros_like(x, dtype=bool)
        z = (x - mean) / std
        return np.abs(z) > 3

    def detect_outliers_mad(x):
        median = np.median(x)
        mad = np.median(np.abs(x - median))
        if mad == 0:
            return np.zeros_like(x, dtype=bool)
        modified_z = 0.6745 * (x - median) / mad
        return np.abs(modified_z) > 3.5

    for col in df.columns:
        series = df[col]
        n = len(series)

        na_count = series.isna().sum()
        na_prop = na_count / n

        outlier_count = np.nan
        outlier_prop = np.nan

        if pd.api.types.is_numeric_dtype(series):
            clean = series.dropna().values

            if len(clean) > 0:
                method = outlier_method

                if outlier_method == "auto":
                    mean = np.mean(clean)
                    std = np.std(clean, ddof=0)
                    if std == 0:
                        method = "iqr"
                    else:
                        skew = np.mean(((clean - mean) / std) ** 3)
                        method = "zscore" if abs(skew) < 1 else "iqr"

                if method == "iqr":
                    outliers = detect_outliers_iqr(clean)
                elif method == "zscore":
                    outliers = detect_outliers_zscore(clean)
                elif method == "mad":
                    outliers = detect_outliers_mad(clean)

                outlier_count = int(np.sum(outliers))
                outlier_prop = outlier_count / len(clean)

        row = {
            "column": col,
            "na_count": na_count,
            "na_proportion": na_prop,
            "outlier_count": outlier_count,
            "outlier_proportion": outlier_prop,
        }

        # Risk levels
        if return_risk:
            if na_prop >= na_threshold:
                na_risk = "high"
            elif na_prop > 0:
                na_risk = "medium"
            else:
                na_risk = "low"

            if pd.isna(outlier_prop):
                outlier_risk = "not_applicable"
            elif outlier_prop >= outlier_threshold:
                outlier_risk = "high"
            elif outlier_prop > 0:
                outlier_risk = "medium"
            else:
                outlier_risk = "low"

            row["na_risk"] = na_risk
            row["outlier_risk"] = outlier_risk

        # Output Suggestions
        if return_suggestions:
            suggestions = []

            if na_prop >= na_threshold:
                suggestions.append("Consider imputation or dropping this column.")

            if pd.notna(outlier_prop) and outlier_prop >= outlier_threshold:
                suggestions.append("Investigate outliers or consider transformation.")

            row["suggestions"] = "; ".join(suggestions) if suggestions else "None"

        results.append(row)

    return pd.DataFrame(results)
