import unittest
from calculator import *

class TestBasicFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_taylor_sin(self):
        self.assertAlmostEqual(taylor_sin(0), 0, places=5)
        self.assertAlmostEqual(taylor_sin(1.57), 1, places=1)

    def test_taylor_cos(self):
        self.assertAlmostEqual(taylor_cos(0), 1, places=5)
        self.assertAlmostEqual(taylor_cos(3.14), -1, places=1)

    def test_taylor_ln(self):
        self.assertAlmostEqual(taylor_ln(1), 0, places=5)

        with self.assertRaises(ValueError):
            taylor_ln(-1)

    def test_abs_value(self):
        self.assertEqual(abs_value(5), 5)
        self.assertEqual(abs_value(-3), 3)
        self.assertEqual(abs_value(0), 0)

    def test_taylor_sqrt(self):
        self.assertAlmostEqual(taylor_sqrt(0), 0, places=5)
        self.assertAlmostEqual(taylor_sqrt(4), 2, places=5)
        self.assertAlmostEqual(taylor_sqrt(9), 3, places=5)

class TestIntegration(unittest.TestCase):

    def test_negative_x_case(self):
        x = -0.1
        result = main_function(x)
        self.assertGreaterEqual(result, 0)

    def test_division_by_zero_positive(self):
        with self.assertRaises(ValueError):
            main_function(0)  

    def test_positive_x_case(self):
        x = 0.5
        result = main_function(x)
        self.assertTrue(isinstance(result, float))

    def test_special_cases(self):
        # Тест для x = 0 (дополнительная проверка)
        with self.assertRaises(ValueError):
            main_function(0)

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            main_function(-1.0)

if __name__ == '__main__':
    unittest.main()