from simple_calculator_python.simple_calculator import BaseCalculator


class MathOperation(BaseCalculator):
    def addition(self, number1, number2):
        result = number1 + number2
        self.store_value(result)
        return result

    def subtraction(self, number1, number2):
        result = number1 - number2
        self.store_value(result)
        return result

    def multiplication(self, number1, number2):
        result = number1 * number2
        self.store_value(result)
        return result

    def division(self, number1, number2):
        try:
            result = number1 / number2
            self.store_value(result)
            return result
        except ZeroDivisionError:
            print("Error: Can't divide by zero")
            return self.value
