"""
Functions to support automated exploratory data analysis (EDA)
"""

import pandas as pd
import numpy as np


def get_summary_df(df, categorical_columns, numerical_columns):
    """
    Returns a summary dataframe with the main statistics, datatypes,
    counts/missing values for numerical and categorical columns.

    For categorical columns, the summary includes:
    - Data types
    - Number of non-null values
    - Count of missing values
    - Most common value/category

    For numerical columns, the summary includes:
    - Data types
    - Count of non-null values
    - Count of missing values
    - Mean
    - Standard deviation
    - Minimum value
    - Maximum value

    Parameters:
    df: Pandas DataFrame.
    categorical_columns: names of the columns with categorical data.
    numerical_columns: names of the columns with numerical data.

    Returns:
    categorical_df: summary dataframe for categorical columns.
    numerical_df: summary dataframe for numerical columns.
    """
    categorical_df = pd.DataFrame()
    numerical_df = pd.DataFrame()
    if categorical_columns == [] or numerical_columns == []:
        raise ValueError("No columns provided to attain a summary")

    for column in categorical_columns:
        if df.loc[:, column].dtype not in ["object", "string"]:
            raise ValueError(f"This is not a categorical column: {column}")
        else:
            categorical_df[column] = pd.DataFrame(
                [
                    df.loc[:, column].dtypes,
                    df.loc[:, column].count(),
                    np.sum(df.loc[:, column].isnull()),
                    # Reference: https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column
                    df.loc[:, column].mode()[0],
                ]
            )

    for column in numerical_columns:
        if df.loc[:, column].dtype not in ["int64", "float64"]:
            raise ValueError(f"This is not a numerical column: {column}")
        else:
            numerical_df[column] = pd.DataFrame(
                [
                    df.loc[:, column].dtypes,
                    df.loc[:, column].count(),
                    np.sum(df.loc[:, column].isnull()),
                    df.loc[:, column].mean(),
                    df.loc[:, column].std(),
                    df.loc[:, column].min(),
                    df.loc[:, column].max(),
                ]
            )
    categorical_df, numerical_df = categorical_df.transpose(), numerical_df.transpose()
    categorical_df.columns = [
        "Data Type",
        "Non-Null Count",
        "Missing Values Count",
        "Most Common Value",
    ]
    numerical_df.columns = [
        "Data Type",
        "Non-Null Count",
        "Missing Values Count",
        "Mean",
        "Std",
        "Min",
        "Max",
    ]
    return categorical_df, numerical_df
