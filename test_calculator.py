import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        # Ajoutez plus de tests pour différents cas

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        # Ajoutez plus de tests pour différents cas

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        # Ajoutez plus de tests pour différents cas

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertRaises(ValueError, self.calculator.divide, 6, 0)
        # Ajoutez plus de tests pour différents cas

if __name__ == '__main__':
    unittest.main()
