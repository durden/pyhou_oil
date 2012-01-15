#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import sys
from PyQt4 import QtGui
import PyQt4.Qwt5 as Qwt
import numpy as np


def qwt():
    """Show data in qwt plot"""

    plot = Qwt.QwtPlot()
    plot.setTitle("Oil Production by Year")
    curve = Qwt.QwtPlotCurve("Barrels (in thousands)")

    x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
    y = np.arange(-2 * np.pi, 2 * np.pi, 0.01)

    curve.setData(x, y)
    curve.attach(plot)
    plot.replot()

    return plot


def main():
    """main"""

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    window.setCentralWidget(qwt())
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
