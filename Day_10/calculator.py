class Calculator:
    # TODO: Define the add method (takes self, n1, n2 and returns n1 + n2)
    def add(self, n1, n2):
        """Adds two numbers (n1 and n2)"""
        return n1 + n2

    # TODO: Define the subtract method (takes self, n1, n2 and returns n1 - n2)
    def subtract(self, n1, n2):
        """Subtracts two numbers (n1 and n2)"""
        return n1 - n2

    # TODO: Define the multiply method (takes self, n1, n2 and returns n1 * n2)
    def multiply(self, n1, n2):
        """Multiply two numbers (n1 and n2)"""
        return n1 * n2

    # TODO: Define the divide method (takes self, n1, n2 and returns n1 / n2)
    def divide(self, n1, n2):
        """Divide two numbers (n1 and n2)"""
        if n2 == 0:
            raise ValueError("Error! Zero Divison!")
        return n1 / n2
    # Hint: Remember to check for division by zero!


