#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import datetime
import sys

from PyQt4 import QtGui
import PyQt4.Qwt5 as Qwt

import tables

import conversion


class TimeScaleDraw(Qwt.QwtScaleDraw):
    """Scale to display time values in month/year"""

    def label(self, value):
        """
        Convert time value into string-friendly label to be placed on a plot
        """

        super(TimeScaleDraw, self).label(value)

        date = datetime.datetime.fromtimestamp(value)
        return Qwt.QwtText((date.strftime("%b/%Y")))


class StateProductionDialog(QtGui.QDialog):
    """Dialog to plot oil production by state"""

    def __init__(self, plot, parent):
        """init"""

        super(StateProductionDialog, self).__init__(parent)

        hlayout = QtGui.QHBoxLayout()
        hlayout.setMargin(0)
        hlayout.addWidget(plot)
        self.setLayout(hlayout)

def plot_production_by_month():
    """Show data in qwt plot"""

    plot = Qwt.QwtPlot()
    plot.setTitle("Oil Production by Month")
    plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
    plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

    # Need custom scale to set labels to month/year
    plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

    hdf5 = tables.openFile(conversion.HDF5_FILENAME)
    x_vals = []
    y_vals = []

    for row in hdf5.root.data.production_by_month:
        y_vals.append(row[0])
        x_vals.append(row[1])

    curve = Qwt.QwtPlotCurve("Barrels (in thousands)")
    curve.attach(plot)
    curve.setData(x_vals, y_vals)

    plot.replot()

    return plot

def plot_production_by_state():
    """Show data in qwt plot"""

    plot = Qwt.QwtPlot()
    plot.setTitle("Oil Production by Month")
    plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
    plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

    # Need custom scale to set labels to month/year
    plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

    hdf5 = tables.openFile(conversion.HDF5_FILENAME)
    la_vals = []
    tx_vals = []
    ak_vals = []
    ca_vals = []
    y_vals = []

    y_vals = hdf5.root.data.production_by_state_month.cols.date[:]
    la_vals = hdf5.root.data.production_by_state_month.cols.la_barrels[:]
    tx_vals = hdf5.root.data.production_by_state_month.cols.tx_barrels[:]
    ak_vals = hdf5.root.data.production_by_state_month.cols.ak_barrels[:]
    ca_vals = hdf5.root.data.production_by_state_month.cols.ca_barrels[:]

    curve = Qwt.QwtPlotCurve("La")
    curve.attach(plot)
    curve.setData(la_vals, y_vals)

    curve = Qwt.QwtPlotCurve("Tx")
    curve.attach(plot)
    curve.setData(tx_vals, y_vals)

    curve = Qwt.QwtPlotCurve("Ak")
    curve.attach(plot)
    curve.setData(ak_vals, y_vals)

    curve = Qwt.QwtPlotCurve("Ca")
    curve.attach(plot)
    curve.setData(ca_vals, y_vals)

    plot.replot()

    return plot


def main():
    """main"""

    # Convert data then we can interface with pytables exclusively
    conversion.convert_xls_to_hdf5(conversion.XLS_FILENAME,
                                                conversion.HDF5_FILENAME)
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    window.setCentralWidget(plot_production_by_month())
    window.show()

    state_prod_window = StateProductionDialog(plot_production_by_state(),
                                                                        window)
    state_prod_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
