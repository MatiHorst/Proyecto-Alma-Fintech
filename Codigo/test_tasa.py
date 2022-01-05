"""
test_tasa.py
Modulo para realizar test unitario al calculo de las tasas implícitas.
"""

import unittest
from tasas import calculoTasa

class TestTasas(unittest.TestCase):
    def test_calculoTasa(self):
        self.assertEqual(calculoTasa(178.03, 208), 61.44)


if __name__ == '__main__':
    unittest.main()
