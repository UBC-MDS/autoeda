# MIT License
#
# Copyright (c) 2026 Eli Gonzalez, Gurleen Kaur, Gloria Yi, Mantram Sharma
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Add a docstring here for the init module.

This might include a very brief description of the package,
its purpose, and any important notes.
"""
from .get_summary_df import get_summary_df
from .check_na_outlier import check_na_outliers
from .inspect import get_unary
from .inspect import get_high_cardinality
from .plot import plot_correlation_heatmap
from .plot import plot_histograms_by_target

__all__ = [
    "get_summary_df",
    "check_na_outliers",
    "get_unary",
    "get_high_cardinality",
    "plot_correlation_heatmap",
    "plot_histograms_by_target",
]
