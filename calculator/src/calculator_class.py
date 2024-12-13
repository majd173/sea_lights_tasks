import json


class Calculator:
    """
    This class manages different function on maths processes.
    """
    pass

    @staticmethod
    def addition_function(a, b):
        """
        This function manages addition process.
        :param a:
        :param b:
        :return: addition result
        """
        if a is not None and b is not None:
            result = a + b
            print(f'{a} + {b} = {result}')
            return result
        else:
            return None

    @staticmethod
    def subtraction_function(a, b):
        """
        This function manages addition process.
        :param a:
        :param b:
        :return: subtraction result
        """
        if a is not None and b is not None:
            result = a - b
            print(f'{a} - {b} = {result}')
            return result
        else:
            return None

    @staticmethod
    def multiplication_function(a, b):
        """
        This function manages multiplication process.
        :param a:
        :param b:
        :return: multiplication result
        """
        if a is not None and b is not None:
            result = a * b
            print(f'{a} + {b} = {result}')
            return result
        else:
            return None

    @staticmethod
    def division_function(a, b):
        """
        This function manages division process.
        :param a:
        :param b:
        :return: division result
        """
        if a is not None and b is not None:
            if b != 0:
                result = a / b
                print(f'{a} / {b} = {result}')
                return a / b
            return "Wrong! division by zero"

