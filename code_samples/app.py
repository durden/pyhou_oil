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

        date = datetime.datetime.fromtimestamp(value)
        return Qwt.QwtText((date.strftime("%b/%Y")))


def qwt():
    """Show data in qwt plot"""

    plot = Qwt.QwtPlot()
    plot.setTitle("Oil Production by Year")
    plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
    plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

    plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

    curve = Qwt.QwtPlotCurve("Barrels (in thousands)")

    f = tables.openFile(conversion.HDF5_FILENAME)
    x_vals = []
    y_vals = []

    for row in f.root.data.production:
        y_vals.append(row[0])
        x_vals.append(row[1])

    curve.attach(plot)
    curve.setData(x_vals, y_vals)
    plot.replot()

    return plot


def main():
    """main"""

    # Convert data then we can interface with pytables exclusively
    conversion.convert_xls_to_hdf5(conversion.XLS_FILENAME,
                                                    conversion.HDF5_FILENAME)
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    window.setCentralWidget(qwt())
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
