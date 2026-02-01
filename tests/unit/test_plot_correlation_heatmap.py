import pandas as pd
import matplotlib
import pytest
import autoeda.plot as plot


def test_plot_correlation_heatmap_basic():
    # Create a simple numeric dataframe
    """Test heatmap generation on a simple numeric dataframe."""
    df = pd.DataFrame(
        {
            "age": [22, 25, 30, 35],
            "income": [40000, 50000, 60000, 70000],
            "score": [60, 65, 70, 75],
        }
    )

    ax = plot.plot_correlation_heatmap(df)

    # Check that the function returns a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)


def test_plot_correlation_heatmap_ignores_non_numeric():
    """Test that ensure non-numeric columns are ignored when computing correlations."""
    df = pd.DataFrame(
        {
            "age": [22, 25, 30, 35],
            "income": [40000, 50000, 60000, 70000],
            "city": ["Toronto", "Vancouver", "Calgary", "Montreal"],
        }
    )

    ax = plot.plot_correlation_heatmap(df)
    assert isinstance(ax, matplotlib.axes.Axes)


def test_plot_correlation_heatmap_no_numeric_columns():
    """Test to make sure ValueError is raised when no numeric columns are present"""
    df = pd.DataFrame(
        {
            "city": ["Toronto", "Vancouver", "Calgary"],
            "country": ["Canada", "Canada", "Canada"],
        }
    )

    with pytest.raises(ValueError):
        plot.plot_correlation_heatmap(df)


def test_plot_correlation_heatmap_handles_nans():
    """
    test to make sure NAN values are not breaking the
    heatmap by dropping those values
    """
    df = pd.DataFrame(
        {
            "age": [22, 25, None, 35],
            "income": [40000, None, 60000, 70000],
            "score": [60, 65, 70, None],
        }
    )

    ax = plot.plot_correlation_heatmap(df)

    assert isinstance(ax, matplotlib.axes.Axes)
