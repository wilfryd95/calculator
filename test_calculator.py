import unittest
from calculator import calculator

class TestCalculatrice(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator("1 + 1"), 2)

    def test_soustraction(self):
        self.assertEqual(calculator("2 - 1"), 1)

    def test_multiplication(self):
        self.assertEqual(calculator("3 * 3"), 9)

    def test_division(self):
        self.assertEqual(calculator("10 / 2"), 5)

    def test_division_par_zero(self):
        self.assertEqual(calculator("5 / 0"), "Erreur: division by zero")

    def test_expression_invalide(self):
        resultat = calculator("deux plus deux")
        self.assertTrue(resultat.startswith("Erreur: invalid syntax"))


if __name__ == '__main__':
    unittest.main()
