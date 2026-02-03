import pandas as pd
import numpy as np


def get_summary_df(df, categorical_columns, numerical_columns):
    """
    Returns a summary dataframe with the main statistics, datatypes,
    counts/missing values for numerical and categorical columns.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset for exploratory data analysis.
    categorical_columns : list of str
        Names of columns treated as categorical variables.
    numerical_columns : list of str
        Names of columns treated as numerical variables.

    Returns
    -------
    categorical_df : pandas.DataFrame
        Summary dataframe for categorical columns, including:
        data types, non-null counts, missing values, and
        most frequent category.
    numerical_df : pandas.DataFrame
        Summary dataframe for numerical columns, including:
        data types, non-null counts, missing values,
        mean, standard deviation, minimum, and maximum values.
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
    categorical_df = categorical_df.transpose()
    numerical_df = numerical_df.transpose()
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
