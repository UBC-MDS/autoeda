---
editor: 
  markdown: 
    wrap: 72
---

# Welcome to AutoEDA's Documentation '

## Overview

**autoeda** is a Python package for automated exploratory data analysis
(EDA). It provides simple, reusable functions to inspect datasets,
summarize variables, and generate quick diagnostics for tabular data.

## Installation

Install the package using pip:

```{bash}
pip install autoeda
```

## Quick Start

Here is a minimal example showing how to use autoeda on a pandas
DataFrame:

```{python}

import pandas as pd from autoeda.inspect import inspect_df

df = pd.DataFrame({ "age": [23, 45, 31], "income": [50000, 80000, 62000] })

inspect_df(df)
```

## What’s Included

autoeda currently provides the following functionality:

-   Dataset inspection utilities
-   Summary statistics for numerical and categorical variables
-   Quick diagnostics for tabular datasets

::: {toctree}
:maxdepth: 2 :hidden: :caption: Contents:

Home <self>
:::

This is the landing page of your docs. you can update it as you'd like
to. This documentation example uses myst markdown as the primary
documentation syntax.

::: {button-link}
<https://www.pyopensci.org/python-package-guide/documentation/hosting-tools/myst-markdown-rst-doc-syntax.html>
:color: primary :class: sd-rounded-pill float-left

Learn more about myst in our pyOpenSci packaging guide.
:::

Myst is a version of markdown that has more formatting flexibility. This
is what a sphinx directive looks like using myst markdown formatting:

``` markdown
:::{toctree}
:maxdepth: 2
:caption: Contents:
:::
```

If you see syntax like the syntax below, you are looking at rst.

``` rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:
```

## Copyright

-   Copyright © 2026 Eli Gonzalez, Gurleen Kaur, Gloria Yi, Mantram
    Sharma.
-   Free software distributed under the MIT License.
