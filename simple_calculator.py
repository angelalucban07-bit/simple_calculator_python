#parent class
class lculator:
    def get_numbers(self):
        while True:
            try:
                number1 = int(input("Enter a number: "))
                number2 = int(input("Enter another number: "))
                return number1, number2
            except ValueError:
                print("Invalid input. Please Enter numbers only.")

class Operation(lculator):
    def addition(self, number1, number2):
        return number1 + number2
    def subtraction(self, number1, number2):
        return number1 - number2
    def multiplication(self, number1, number2):
        return number1 * number2
    def division(self, number1, number2):
        return number1/ number2

    #will add subtract, multiply, and divide methods here...
