"""Plot fitting result."""
import numpy as np
from eddington import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    errorbar,
    plot,
)


def plot_fitting(  # pylint: disable=C0103,R0913
    func,
    data: FitData,
    plot_configuration: PlotConfiguration,
    a: np.ndarray,
    step: float = None,
):
    """
    Plot fitting plot.

    :param func: Fitting function.
    :param data: Fitting data
    :param plot_configuration: Plot configuration
    :param a: The parameters result
    :param step: float or None. step between values of the continuous plot
    """
    fig = get_figure(
        title_name=plot_configuration.title, plot_configuration=plot_configuration
    )
    errorbar(fig=fig, x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    if step is None:
        step = (plot_configuration.xmax - plot_configuration.xmin) / 1000.0
    x = np.arange(  # pylint: disable=C0103
        plot_configuration.xmin, plot_configuration.xmax, step=step
    )
    y = func(a, x)  # pylint: disable=C0103
    plot(fig=fig, x=x, y=y)
    return fig
