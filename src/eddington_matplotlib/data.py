"""Plot fitting data."""
from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    errorbar,
    show_or_export,
)


def plot_data(data: FitData, plot_configuration: PlotConfiguration, output_path=None):
    """
    Plot fitting data.

    :param data: Fitting data
    :param plot_configuration: Plot configuration
    :param output_path: Path or None. output path to save the plot.
    """
    fig = get_figure(
        title_name=plot_configuration.data_title, plot_configuration=plot_configuration
    )
    errorbar(fig=fig, x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    show_or_export(fig=fig, output_path=output_path)
