"""
Unit tests for the get_summary_df function.

These tests check that the get_summary_df function
works correctly on the proper data, and also returns
errors for the incorrectly defined arguments.
"""

import pandas as pd
import numpy as np
import pytest

from src.autoeda.get_summary_df import get_summary_df

df = pd.DataFrame({
        'name': ['John', 'Jeffery', 'Alice', 'Sam', 'Millie'],
        'age': [25, 30, 18, 27, 45],
        'education': ['Undergrad', 'Grad', 'Undergrad', 'PhD', 'Undergrad'],
        'salary': [70000.0, 90000.0, 75000.0, 120000.0, 80000.0]
    })

def test_get_summary_df_small_dataset():
    '''
    This test checks if the get_summary_df function correctly processes 
    a small dataset
    '''
    categorical_columns = ['name', 'education']
    numerical_columns = ['age', 'salary']

    summary = get_summary_df(df, categorical_columns, numerical_columns)
    assert isinstance(summary, tuple)
    assert len(summary) == 2
    assert isinstance(summary[0], pd.DataFrame)

def test_get_summary_df_no_columns():
    '''
    This test checks if we get the appropriate error when categorical 
    and numerical columns are not defined
    '''
    categorical_columns = []
    numerical_columns = []

    with pytest.raises(ValueError):
        get_summary_df(df, categorical_columns, numerical_columns)

def test_get_summary_df_incorrect_categorical_column_types():
    '''
    This test checks if we get the appropriate error when incorrect 
    column types in categorical_columns is provided
    '''
    categorical_columns = ['name', 'education', 'salary']
    numerical_columns = ['age']

    with pytest.raises(ValueError):
        get_summary_df(df, categorical_columns, numerical_columns)

def test_get_summary_df_incorrect_numerical_column_types():
    '''
    This test checks if we get the appropriate error when incorrect 
    column types in numerical_columns is provided
    '''
    categorical_columns = ['name']
    numerical_columns = ['age', 'salary', 'education']

    with pytest.raises(ValueError):
        get_summary_df(df, categorical_columns, numerical_columns)