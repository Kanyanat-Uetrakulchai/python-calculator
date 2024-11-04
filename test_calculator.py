import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_nagative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_substract_nagative(self):
        self.assertEqual(self.calc.subtract(-4, -1), -3)

    def test_substract_zero(self):
        self.assertEqual(self.calc.subtract(1, 0), 1)

    def test_multiply_nagative(self):
        self.assertEqual(self.calc.multiply(-1, -4), 4)

    def test_multipy_zero(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)

    def test_divide_nagative(self):
        self.assertEqual(self.calc.divide(-4, -2), 2)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(0, 1), 0)
    
    def test_modulo_nagative(self):
        self.assertEqual(self.calc.modulo(-32, -5), 2)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(1, 0), 1)

if __name__ == '__main__':
    unittest.main()