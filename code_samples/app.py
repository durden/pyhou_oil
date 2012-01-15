#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import sys
from PyQt4 import QtGui

def main():
    """main"""

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Oil Production')
    w.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
