
class PyQtCalcModel():

    ERROR_MSG = 'ERROR'

    # Create a Model to handle the calculator's operation
    def evaluateExpression(self, expression):
        """Evaluate an expression."""
        try:
            result = str(eval(expression, {}, {}))
            #  eval() to evaluate a string as an expression
            # it is very dangerous
        except Exception:
            result = self.ERROR_MSG

        return result