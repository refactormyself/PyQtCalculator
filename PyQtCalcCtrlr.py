
from functools import partial
from PyQtCalcModel import PyQtCalcModel

class PyQtCalcCtrlr:
    """Calculator Controller class."""
    def __init__(self, model, view):
        
        self._view = view
        self._evaluate = model.evaluateExpression

        self._connectSignals()
    
    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == PyQtCalcModel.ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', '\u001B', '\u221a', '\u00B1'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        # self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['\u001B'].clicked.connect(lambda : self._view.showStatus("NOT YET IMPLEMENTED !!!"))
        self._view.buttons['\u221a'].clicked.connect(lambda : self._view.showStatus("NOT YET IMPLEMENTED !!!"))
        self._view.buttons['\u00B1'].clicked.connect(lambda : self._view.showStatus("NOT YET IMPLEMENTED !!!"))
        
        # C - clears display and buffer
        # '\u001B'(backspace) - clears last xter in buffer and update display
        # '=' - calculate result and clears buffer
        #     - causes non-zero text => value and 0 => text 
        # {*,/,%,+,-,^,} - require 1 value (non-zero text) to be present (only report error)
        #                - causes non-zero text => value and 0 => text 
        #                - is displayed in DisplayExpr
        #                - 
        # "."
        # "()"
        # {0..9}
        # '\u221a' (square root)
        # '\u00B1' (toggle sign)
