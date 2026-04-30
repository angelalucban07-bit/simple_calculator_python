#parent class
class BaseCalculator:
    def get_numbers(self):
        while True:
            try:
                number1 = int(input("Enter a number: "))
                number2 = int(input("Enter another number: "))
                return number1, number2
            except ValueError:
                print("Invalid input. Please Enter numbers only.")
#child class
class MathOperations(BaseCalculator):
    def addition(self, number1, number2):
        return number1 + number2
    def subtraction(self, number1, number2):
        return number1 - number2
    def multiplication(self, number1, number2):
        return number1 * number2
    def division(self, number1, number2):
        try:
            return number1 / number2
        except ZeroDivisionError:
        print("Error: Can't divide by zero")

#another class for the main loop to display the menu
class CalculatorInterface:
    def __init__(self):
        self.operations = MathOperations()

    def run(self):
        while True:
            print("\n=== Calculator ===")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Enter your choice: ")

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid input. Please Enter only one of the following values (1-4):")
                continue
#di muna tapos xori po
#will learn better methods for better main display