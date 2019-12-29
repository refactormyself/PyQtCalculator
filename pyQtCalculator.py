#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QSystemTrayIcon

from PyQtCalcView import PyQtCalcView
from PyQtCalcCtrlr import PyQtCalcCtrlr
from PyQtCalcModel import PyQtCalcModel

__version__ = '0.00a1'
__author__ = 'Bolarinwa Saheed'

def main():
    
    pyqtcalc = QApplication(sys.argv)
    view = PyQtCalcView()
    view.show()

    # trayIcon = QSystemTrayIcon(app_icon, view)
    # trayIcon.show()    

    model = PyQtCalcModel()
    PyQtCalcCtrlr(model=model, view=view)
        
    sys.exit(pyqtcalc.exec_())

if __name__ == '__main__':
    main()
