# fns_and_dsa/test_arithmetic_operations.py

import unittest
from arithmetic_operations import perform_operation

class TestArithmeticOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(perform_operation(5, 6, "add"), 11)

    def test_subtraction(self):
        self.assertEqual(perform_operation(10, 3, "subtract"), 7)

    def test_multiplication(self):
        self.assertEqual(perform_operation(4, 7, "multiply"), 28)

    def test_division(self):
        self.assertEqual(perform_operation(20, 4, "divide"), 5.0)

    def test_division_by_zero(self):
        self.assertEqual(perform_operation(8, 0, "divide"), "Error: Division by zero")

    def test_invalid_operation(self):
        self.assertEqual(perform_operation(9, 3, "mod"), "Error: Invalid operation")

if __name__ == "__main__":
    unittest.main()

