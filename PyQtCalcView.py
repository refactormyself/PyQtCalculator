from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QWidget,
    QStackedWidget, QStatusBar, QLabel, QFrame
    )
from PyQt5.QtCore import pyqtSlot, QRect


class PyQtCalcView(QMainWindow):
    """View of the Calculator (GUI)."""
    def __init__(self):
        super().__init__()

        # setup and properties
        self.setWindowTitle('Calculator - Made with PyQt')
        self.setFixedSize(205, 305)
        app_icon = QIcon(r'_PY\calculator\calculator-40.png')
        self.setWindowIcon(app_icon)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        # Create the actual display
        self._createMainDisplay()
        self._createButtons()
        self._createMenu()
        self._createStatusBar()

    
    def _createMainDisplay(self):
        
        # self.displaybox = QFrame(self)
        # self.displaybox.setGeometry(QRect(5, 25, 195, 70))
        # self.displaybox.setStyleSheet("margin-bottom: 20px; border: 0px; border-radius: 10px; background: blue; color: white;")
        
        self.display_expr = QLabel() #(self.displaybox)
        self.display_expr.wordWrap = False
        # self.display_expr.height = 35
        self.display_expr.setAlignment(Qt.AlignRight)
        self.display_expr.setStyleSheet("margin:0px;border:0px;Background-color:blue;color:white")
        self.generalLayout.addWidget(self.display_expr)
        expr_font = QtGui.QFont("Times", 8, italic=True)
        self.display_expr.setFont(expr_font)
        # self.display_expr.setText("self.display_expr")

        self.display = QLabel() #(self.displaybox)
        self.display.setWordWrap(False)
        # self.display.height = 45
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("border:0px;Background-color:blue;color:white")
        self.generalLayout.addWidget(self.display)
        result_font = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        self.display.setFont(result_font)
        # self.display.setText("self.display")

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createStatusBar(self):
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Basic Calculator")
        self.setStatusBar(self.status_bar)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        
        buttons = {'\u001B': (0, 0),
                   'C': (0, 1),
                   '(': (0, 2),
                   ')': (0, 3),
                   '\u221a': (0, 4),
                   '7': (1, 0),
                   '8': (1, 1),
                   '9': (1, 2),
                   '/': (1, 3),
                   '%': (1, 4),
                   '4': (2, 0),
                   '5': (2, 1),
                   '6': (2, 2),
                   '*': (2, 3),
                   '^': (2, 4),
                   '1': (3, 0),
                   '2': (3, 1),
                   '3': (3, 2),
                   '-': (3, 3),
                   '\u00B1': (3, 4),
                   '0': (4, 0),
                   '00': (4, 1),
                   '.': (4, 2),
                   '+': (4, 3),
                   '=': (4, 4),
                  }
        
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(30, 30)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
                        
        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

    def showStatus(self, message):
        """Show message on the status bar."""
        self.status_bar.showMessage(message)

        