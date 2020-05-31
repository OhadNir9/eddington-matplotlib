"""Utility functions for plotting."""
import matplotlib.pyplot as plt


def get_figure():
    """Gets a figure from matplotlib."""
    return plt.figure()


def plot(x, y, fig):
    """
    Plot y as a function of x.

    :param x: X values
    :param y: Y values
    :param fig: Plot figure
    """
    plt.plot(x, y, figure=fig)


def horizontal_line(xmin, xmax, y=0):
    """
    Add horizontal line to figure.

    :param xmin: Minimum x value of line
    :param xmax: Maximum x value of line
    :param y: The y value of the line
    """
    plt.hlines(y, xmin=xmin, xmax=xmax, linestyles="dashed")


def errorbar(x, y, xerr, yerr, fig):
    """
    Plot error bar to figure.

    :param x: X values
    :param y: Y values
    :param xerr: Errors of x
    :param yerr: Errors of y
    :param fig: Plot figure
    """
    plt.errorbar(
        x=x,
        y=y,
        xerr=xerr,
        yerr=yerr,
        markersize=1,
        marker="o",
        linestyle="None",
        figure=fig,
    )


def title(title_name, fig):
    """
    Add/remove title to figure.

    :param title_name: str or None. If None, don't add title. otherwise, add given title
    :param fig: Plot figure.
    """
    if title_name is not None:
        plt.title(title_name, figure=fig)


def label_axes(xlabel, ylabel, fig):
    """
    Add/remove labels to figure.

    :param xlabel: str or None. If None, don't add label. otherwise, add given label
    :param ylabel: str or None. If None, don't add label. otherwise, add given label
    :param fig: Plot figure.
    """
    if xlabel is not None:
        plt.xlabel(xlabel, figure=fig)
    if ylabel is not None:
        plt.ylabel(ylabel, figure=fig)


def grid(is_grid, fig):
    """
    Add/remove grid to figure.

    :param is_grid: Boolean. add or remote grid to plot
    :param fig: Plot figure
    """
    if is_grid:
        plt.grid(True, figure=fig)


def show_or_export(fig: plt.Figure, output_path=None):
    """
    Show plot or export it to a file.
    
    :param fig: a plot figure
    :param output_path: Path or None. if None, show plot. otherwise, save to path.
    """
    if output_path is None:
        plt.show()
        return
    fig.savefig(output_path)
