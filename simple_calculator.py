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

            number1, number2 = self.operations.get_numbers()
            if number1 is None or number2 is None:
                continue
            result = None
#functions
            if choice == "1":
                print(self.operations.addition(number1, number2))
            elif choice == "2":
                print(self.operations.subtraction(number1, number2))
            elif choice == "3":
                print(self.operations.multiplication(number1, number2))
            elif choice == "4":
                print(self.operations.division(number1, number2))

            if result is not None:
                print("The result is:", result)

            again = input("\nDo you want to continue? (y/n): ")
            if again == "n":
                print("Thank you for using the calculator. Goodbye! xoxo")
                break
#run
if __name__ == "__main__":
    calculator = CalculatorInterface()
    calculator.run()
#will learn better methods for better main display