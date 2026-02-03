import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation_heatmap(df, target=None, method="pearson", figsize=(10, 8)):
    """
    Generate a correlation heatmap for numeric features in a dataset.

    This function computes pairwise correlations between numeric columns
    and visualizes them as a heatmap. Optionally, a target column can be
    highlighted to show correlations specifically with the target.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing numeric and non-numeric features.

    target : str, optional
        Name of the target column. If provided, correlations with the target
        may be emphasized or displayed separately.

    method : {"pearson", "spearman", "kendall"}, default="pearson"
        Correlation method to use.

    figsize : tuple, default=(10, 8)
        Size of the heatmap figure.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object containing the heatmap visualization.
    """
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    # Drop NAN rows
    numeric_df = numeric_df.dropna()
    if numeric_df.shape[1] < 2:
        raise ValueError("Not enough numeric data to compute correlation heatmap.")

    # Edge case: no numeric columns
    if numeric_df.shape[1] == 0:
        raise ValueError("No numeric columns found for correlation heatmap.")

    # Compute correlation matrix
    corr = numeric_df.corr(method=method)

    # Create plot
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    return ax


def plot_histograms_by_target(df, target, features=None, bins=30, figsize=(12, 8)):
    """
    Plot histograms of features grouped by a target variable.

    This function visualizes the distribution of selected features
    conditioned on the target variable. This is useful for understanding
    class separation and feature behavior.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing features and target.

    target : str
        Name of the target column.

    features : list of str, optional
        List of feature column names to plot. If None, all numeric
        columns except the target will be used.

    bins : int, default=30
        Number of bins for the histograms.

    figsize : tuple, default=(12, 8)
        Size of the figure.

    Returns
    -------
    matplotlib.figure.Figure
        Figure object containing the histograms.
    """

    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in dataframe.")

    if features is None:
        features = df.select_dtypes(include="number").columns.tolist()
        if target in features:
            features.remove(target)

    if len(features) == 0:
        raise ValueError("No numeric features available for histogram plotting.")

    fig, axes = plt.subplots(len(features), 1, figsize=figsize)

    if len(features) == 1:
        axes = [axes]

    for ax, feature in zip(axes, features):
        for label, group in df.groupby(target):
            ax.hist(group[feature].dropna(), bins=bins, alpha=0.5, label=str(label))

        ax.set_title(feature)
        ax.legend(title=target)

    plt.tight_layout()
    return fig
