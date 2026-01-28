---
editor: 
  markdown: 
    wrap: 72
---

# Welcome to AutoEDA's Documentation '

# Welcome to AutoEDA

**autoeda** is a Python package for automated exploratory data analysis
(EDA). It provides simple, reusable functions to inspect datasets,
summarize variables, and generate quick diagnostics for tabular data.

## Installation

Install the package using pip:

```bash
pip install autoeda
```

## Quick Start

Here is a minimal example showing how to use autoeda on a pandas
DataFrame:

```python
import pandas as pd
from autoeda.inspect import inspect_df

df = pd.DataFrame({
    "age": [23, 45, 31],
    "income": [50000, 80000, 62000]
})

inspect_df(df)

```

## What’s Included

autoeda currently provides the following functionality:

- Dataset inspection utilities
- Summary statistics for numerical and categorical variables
- Quick diagnostics for tabular datasets

::: {toctree}
:maxdepth: 2
:hidden: 
:caption: Contents:

Home <self>
:::

This is the landing page of your docs. you can update it as you'd like
to. This documentation example uses myst markdown as the primary
documentation syntax.

```{button-link} https://www.pyopensci.org/python-package-guide/documentation/hosting-tools/myst-markdown-rst-doc-syntax.html
:color: primary 
:class: sd-rounded-pill float-left

Learn more about myst in our pyOpenSci packaging guide.
```

Myst is a version of markdown that has more formatting flexibility. This
is what a sphinx directive looks like using myst markdown formatting:

## Core Functions

### `inspect_df(df)`

Inspects a pandas DataFrame and returns a concise overview including:

- Column data types
- Missing value counts
- Basic summary statistics

**Example:**

```python

from autoeda.inspect import inspect_df

inspect_df(df)
```

### `get_unary(df, threshold=0.75, dropna=False)`

Identifies columns that are dominated by a single value, which may
indicate low-information or near-constant features.

- `threshold` controls how dominant a value must be to flag a column
- `dropna` controls whether missing values are ignored

**Example:**

```python

from autoeda.inspect import get_unary

get_unary(df)
```

### `get_high_cardinality(df, max_unique_ratio=0.5)`

Identifies columns with a high number of unique values relative to the
size of the dataset, which may require special encoding or handling.

- `max_unique_ratio` defines the maximum allowed ratio of unique
    values

**Example:**

```python

from autoeda.inspect import get_high_cardinality

get_high_cardinality(df)
```

### `get_summary_df(df)`

Generates a summary DataFrame that provides an overview of each column,
including data types, counts, missing values, and basic descriptive
statistics.

**Example:**

```python

 from autoeda.inspect import get_summary_df

get_summary_df(df)
```

### `check_na_outliers(df, outlier_method="auto")`

Checks each column for missing values and potential outliers, helping
identify data quality issues that may require preprocessing.

- `outlier_method` controls how outliers are detected

**Example:**

```python

from autoeda.inspect import check_na_outliers

check_na_outliers(df)
```

### `plot_correlation_heatmap(df, target=None, method="pearson")`

Creates a correlation heatmap for numerical features in the dataset to
help identify relationships between variables. If a target variable is
provided, correlations with the target are highlighted.

- `target` optionally specifies a target column
- `method` controls the correlation metric used

**Example:**

```python

from autoeda.inspect import plot_correlation_heatmap

plot_correlation_heatmap(df)
```

::: {toctree}
:maxdepth: 2
:caption: Contents:
:::

```text
If you see syntax like the syntax below, you are looking at rst.
```

## Copyright

- Copyright © 2026 Eli Gonzalez, Gurleen Kaur, Gloria Yi, Mantram
    Sharma.
- Free software distributed under the MIT License.
