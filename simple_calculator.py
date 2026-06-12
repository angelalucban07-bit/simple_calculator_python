class BaseCalculator:
    def __init__(self):
        self.value = None

    def store_value(self, result):
        self.value = result #this uses last result

#run
if __name__ == "__main__":
    calculator = CalculatorInterface()
    calculator.run()