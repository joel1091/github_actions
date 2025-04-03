import unittest


from main import sumar


class TestCalculadoraFunctions(unittest.TestCase):
    def test_sumar(self):
        """Test de la función sumar"""
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(2.5, 3.5), 6.0)


if __name__ == '__main__':
    unittest.main()
