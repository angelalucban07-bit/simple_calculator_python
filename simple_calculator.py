#trying new functions for storing the value so will have to do a lot more revisions. did not include history
#so deleted the def history because it was unnecessary
from python_practice_programs.isupper_alternative import result


# class BaseCalculator:
#     def get_numbers(self):
#         while True:
#             try:
#                 number1 = int(input("Enter a number: "))
#                 number2 = int(input("Enter another number: "))
#                 return number1, number2
#             except ValueError:
#                 print("Invalid input. Please Enter numbers only.")
#child class
class BaseCalculator:
    def __init__(self):
        self.value = None
        self.memory = []

    def store_value(self, result):
        self.value = result #this uses last result

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

#another class for the main loop to display the menu
class CalculatorInterface:
    def __init__(self):
        self.operations = MathOperation()

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

            # number1, number2 = self.operations.calculate()
            # if number1 is None or number2 is None:
            #     continue
            # result = None

            try:
                if self.operations.value is None:
                    number1 = int(input("Enter the first number: "))
                else:
                    number1 = int(self.operations.value)

                number2 = int(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please Enter only one of the following values (1-4):")
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