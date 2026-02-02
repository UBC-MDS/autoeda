# Welcome to AutoEDA

|  |  |
|----|----|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/autoeda.svg)](https://pypi.org/project/autoeda/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/autoeda.svg)](https://pypi.org/project/autoeda/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI. If you don't plan to publish to PyPI, you can remove them.*

## Overview

AutoEDA is a lightweight Python package designed to automate the most common and time-consuming steps of Exploratory Data Analysis (EDA). Given a pandas DataFrame, AutoEDA quickly surfaces data quality issues, statistical summaries, and meaningful visualizations to help data scientists and analysts understand their data before modeling.

## Installation

### For users:

```{bash}
pip install autoeda
```

### For developers:

```{bash}
git clone https://github.com/Eligoze75/autoeda.git
cd autoeda
conda env create -f environment.yml
conda activate autoeda-dev
pip install -e .
```

## Quick Start

```{python}
import pandas as pd
from autoeda.inspect import inspect_df

df = pd.DataFrame({
    "age": [23, 45, 31],
    "income": [50000, 80000, 62000]
})

inspect_df(df)
```

## Core Functionality

AutoEDA provides a set of modular functions that can be used independently or combined into a full EDA workflow:

-   `inspect` module

    -   `get_unary(df, threshold=0.75, dropna=False)` Identifies columns dominated by a single value beyond a configurable frequency threshold. This helps detect near-constant or low-information features that may be candidates for removal.

    -   `get_high_cardinality(df, max_unique_ratio=0.5)` Identify columns with high cardinality. This helps detect features that may be unsuitable for certain modeling techniques or require special encoding.

-   `get_summary_df(df)`\
    Generates a comprehensive summary table including data types, descriptive statistics, counts, and missing value information for both numerical and categorical features.

-   `check_na_outliers(df, outlier_method="auto", ...)`\
    Diagnoses missing values and potential outliers across columns, optionally assigning qualitative risk levels and actionable suggestions for preprocessing steps such as imputation or transformation.

-   `plot_correlation_heatmap(df, target=None, method="pearson")`\
    Computes and visualizes correlations between numeric features using a heatmap, with optional emphasis on correlations involving a target variable.

-   `plot_histograms_by_target(df, target, features=None)`\
    Plots feature distributions conditioned on a target variable, making it easier to inspect class separation, skewness, and feature behavior across outcomes.

## Positioning in the Python Ecosystem

AutoEDA sits in the space between low-level EDA utilities and fully automated profiling tools. Several existing libraries provide overlapping functionality:

-   [pandas-profiling (renamed as ydata-profiling)](https://docs.profiling.ydata.ai/latest/)

    Generates exhaustive HTML reports but can be heavy, slow on large datasets, and less customizable in programmatic workflows.

-   [Sweetviz](https://github.com/fbdesignpro/sweetviz)

    Focuses on visual comparisons and reporting, primarily for reporting.

-   [D-Tale](https://github.com/man-group/dtale)

    Provides an interactive UI for EDA, but is less suited for scripted pipelines or reproducible analysis.

**AutoEDA** differentiates itself by offering:

-   Simple, composable Python functions (not monolithic reports)
-   Interpretable diagnostics and suggestions
-   Tight integration with pandas and matplotlib/seaborn
-   A focus on EDA as code, suitable for notebooks, scripts, and production pipelines

## Development Setup

Create the environment.

```{bash}
conda env create -f environment.yml 
conda activate autoeda-dev
```

Install the package in editable mode.

``` bash
pip install -e .
```

Run tests

``` bash
pytest
```

## Documentation

For detailed usage instructions, examples, and references, please visit the [AutoEDA documentation website](https://ubc-mds.github.io/autoeda/). The site provides step by step guides and practical examples to help you get the most out of the package.

## Contributors

-   Eli Gonzalez
-   Gloria Yi
-   Gurleen Kaur
-   Mantram Sharma

## Copyright

-   Copyright © 2026 Eli Gonzalez, Gurleen Kaur, Gloria Yi, Mantram Sharma.
-   Free software distributed under the [MIT License](./LICENSE).
