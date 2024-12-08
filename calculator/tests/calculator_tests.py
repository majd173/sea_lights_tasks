import unittest
from sea_lights_tasks.calculator.src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    This class manages tests for Calculator class.
    """

    def test_valid_addition(self):
        """
        This method tests valid addition process.
        """
        self.assertEqual(Calculator.addition_function(
            self, 5, 3), 8, "Wrong result")

    def test_invalid_addition(self):
        """
        THis function tests invalid addition process.
        """
        self.assertNotEqual(Calculator.addition_function(
            self, 5, 3), 7, "Result must be wrong")

    def test_valid_subtraction(self):

        """
        This method tests valid subtraction process.
        """
        self.assertEqual(Calculator.subtraction_function(
            self, 12, 7), 5, "Wrong result")

    def test_invalid_subtraction(self):
        """
        This method tests invalid subtraction process.
        """
        self.assertNotEqual(Calculator.subtraction_function(
            self, 12, 7), 3, "Result must be wrong")

    def test_valid_multiplication(self):
        """
        This method tests valid multiplication process.
        """
        self.assertEqual(Calculator.multiplication_function(
            self, 5, 7), 35, "Wrong result")

    def test_invalid_multiplication(self):
        """
        This method tests invalid multiplication process.
        """
        self.assertNotEqual(Calculator.multiplication_function(
            self, 5, 7), 25, "Result must be wrong")

    def test_valid_division(self):
        """
        This method tests valid division process.
        """
        self.assertEqual(Calculator.division_function(
            self, 12, 4), 3, "Wrong result")

    def test_invalid_division(self):
        """
        This method tests invalid division process.
        """
        self.assertNotEqual(Calculator.division_function(
            self, 12, 4), 2, "Result must be wrong")

    def test_division_by_zero(self):
        """
        This method tests division by zero.
        """
        self.assertEqual(Calculator.division_function(
            self, 7, 0), "Wrong, division by zero", "Wrong result, messages are equal")