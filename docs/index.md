---
title: AutoEDA Documentation
description: Automated EDA tools for fast and clear data exploration.
---

# Welcome to AutoEDA

AutoEDA is a lightweight Python package designed to accelerate exploratory data analysis (EDA) by generating summary statistics, detecting common data issues, and creating useful visualizations.

---

## 📌 Quick Links

- [API Reference](reference/index.md)
- [Installation & Setup](#installation)
- [Usage Examples](#usage-example)
- [Copyright](#copyright)

---

## Installation

```bash
pip install -e .
```

## Usage Example

```python
from autoeda import get_summary_df

summary = get_summary_df(df, target="outcome")
print(summary.head())
```

## Copyright

Copyright © 2026 Eli Gonzalez, Gurleen Kaur, Gloria Yi, Mantram Sharma.

Free software distributed under the MIT License.
