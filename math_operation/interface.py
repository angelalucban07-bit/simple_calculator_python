from math_operation import MathOperation

class CalculatorInterface:
    def __init__(self):
        self.operations = MathOperation()

    def display_result(self):
        print(f"""
╔══════════════════════════════╗
║         🧮 CALCULATOR        
╠══════════════════════════════╣
║  1. ➕ Addition              
║  2. ➖ Subtraction           
║  3. ✖️ Multiplication       
║  4. ➗ Division              
║  5. 🗑️  Clear Memory        
╠══════════════════════════════╣
╠══════════════════════════════╣
║  Stored: {self.operations.value if self.operations.value is not None else "None"}
╚══════════════════════════════╝
""")

    def run(self):
        while True:
            self.display_result()
            choice = input("Choose an operation (1-5): ")

            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid input. Please Enter only one of the following values (1-5):")
                continue

            if choice == "5":
                self.operations.value = None
                print("CLEAR memory")
                continue

            try: #if there is no previous result, directly asks for first input
                if self.operations.value is None:
                    number1 = float(input("Enter the first number: "))
                else:
                    number1 = float(self.operations.value)

                number2 = float(input("Enter the second number: "))

            except ValueError:
                print("Invalid input. Please Enter only one of the following values (1-5):")
                continue

            if choice == "1":
                result = self.operations.addition(number1, number2)
            elif choice == "2":
                result = self.operations.subtraction(number1, number2)
            elif choice == "3":
                result = self.operations.multiplication(number1, number2)
            elif choice == "4":
                result = self.operations.division(number1, number2)

            print(f"Result: {result}")

            again = input("\nDo you want to continue? (y/n): ")
            if again == "n":
                print("Thank you for using the calculator. Goodbye! xoxo")
                break