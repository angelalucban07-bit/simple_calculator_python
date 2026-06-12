class BaseCalculator:
    def __init__(self):
        self.value = None

    def store_value(self, result):
        self.value = result #this uses last result
