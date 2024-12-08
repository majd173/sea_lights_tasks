class Calculator:
    """
    This class manages different function on maths processes.
    """
    pass

    def addition_function(self, a, b):
        if a and b:
            return a + b
        else:
            return None

    def subtraction_function(self, a, b):
        if a and b:
            return a - b
        else:
            return None

    def multiplication_function(self, a, b):
        if a and b:
            return a * b
        else:
            return None

    def division_function(self, a, b):
        try:
            if b != 0:
                return a / b
            else:
                return "Wrong, division by zero"

        except Exception as e:
            return e
