import unittest

from src.lab1.calculator import calculate


class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(10, 5, "+"), 15)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 5, "-"), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(10, 5, "*"), 50)

    def test_division(self):
        self.assertEqual(calculate(10, 5, "/"), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10, 0, "/")

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculate(10, 5, "%")


if __name__ == "__main__":
    unittest.main()