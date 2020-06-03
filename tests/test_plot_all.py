from pathlib import Path
from typing import Dict
from unittest import TestCase
from mock import patch, Mock
import numpy as np

from eddington_matplotlib import PlotConfiguration, OutputConfiguration, plot_all
from tests.base_test_cases import dummy_func


class PlotAllBaseTestCase:

    data = "data"
    xmin = 0.2
    xmax = 9.8
    func = dummy_func
    output_dir = Path("dir/to/output")

    def setUp(self):
        self.result = Mock()
        self.result.a = np.array([1, 2])

        plot_data_patcher = patch("eddington_matplotlib.all.plot_data")
        plot_fitting_patcher = patch("eddington_matplotlib.all.plot_fitting")
        plot_residuals_patcher = patch("eddington_matplotlib.all.plot_residuals")

        self.plot_data = plot_data_patcher.start()
        self.plot_fitting = plot_fitting_patcher.start()
        self.plot_residuals = plot_residuals_patcher.start()

        self.addCleanup(plot_data_patcher.stop)
        self.addCleanup(plot_fitting_patcher.stop)
        self.addCleanup(plot_residuals_patcher.stop)

        self.plot_configuration = PlotConfiguration.build(
            base_name=self.func.name, xmin=self.xmin, xmax=self.xmax, **self.kwargs
        )
        self.output_configuration = OutputConfiguration.build(
            base_name=self.func.name, output_dir=self.output_dir
        )

        plot_all(
            func=self.func,
            data=self.data,
            plot_configuration=self.plot_configuration,
            output_configuration=self.output_configuration,
            result=self.result,
        )

    def test_export_result(self):
        if self.should_export_result:
            self.result.print_or_export.assert_called_once_with(
                self.output_configuration.result_output_path,
            )
        else:
            self.result.export_to_file.assert_not_called()

    def test_plot_data(self):
        if self.should_plot_data:
            self.plot_data.assert_called_once_with(
                data=self.data,
                plot_configuration=self.plot_configuration,
                output_path=self.output_configuration.data_output_path,
            )
        else:
            self.plot_data.assert_not_called()

    def test_plot_fitting(self):
        if self.should_plot_fitting:
            self.plot_fitting.assert_called_once_with(
                func=self.func,
                data=self.data,
                a=self.result.a,
                plot_configuration=self.plot_configuration,
                output_path=self.output_configuration.fitting_output_path,
            )
        else:
            self.plot_fitting.assert_not_called()

    def test_plot_residuals(self):
        if self.should_plot_residuals:
            self.plot_residuals.assert_called_once_with(
                func=self.func,
                data=self.data,
                a=self.result.a,
                plot_configuration=self.plot_configuration,
                output_path=self.output_configuration.residuals_output_path,
            )
        else:
            self.plot_residuals.assert_not_called()


class TestPlotAllDefault(TestCase, PlotAllBaseTestCase):
    kwargs: Dict = dict()

    should_export_result = True
    should_plot_fitting = True
    should_plot_residuals = True
    should_plot_data = False

    def setUp(self):
        PlotAllBaseTestCase.setUp(self)


class TestPlotWithPlotData(TestCase, PlotAllBaseTestCase):
    kwargs = dict(plot_data=True)
    should_export_result = True
    should_plot_fitting = True
    should_plot_residuals = True
    should_plot_data = True

    def setUp(self):
        PlotAllBaseTestCase.setUp(self)


class TestPlotWithoutPlotFitting(TestCase, PlotAllBaseTestCase):
    kwargs = dict(plot_fitting=False)
    should_export_result = True
    should_plot_fitting = False
    should_plot_residuals = True
    should_plot_data = False

    def setUp(self):
        PlotAllBaseTestCase.setUp(self)


class TestPlotWithoutPlotResiduals(TestCase, PlotAllBaseTestCase):
    kwargs = dict(plot_residuals=False)
    should_export_result = True
    should_plot_fitting = True
    should_plot_residuals = False
    should_plot_data = False

    def setUp(self):
        PlotAllBaseTestCase.setUp(self)


class TestPlotWithoutExportResult(TestCase, PlotAllBaseTestCase):
    kwargs = dict(export_result=False)
    should_export_result = False
    should_plot_fitting = True
    should_plot_residuals = True
    should_plot_data = False

    def setUp(self):
        PlotAllBaseTestCase.setUp(self)
