import unittest
import numpy as np
from models.model import gammafun 

class TestGammaFunction(unittest.TestCase):

    def test_gammafun_a_zero(self):
        x = 10
        a = 0
        result = gammafun(x, a)
        self.assertEqual(result, x)

    def test_gammafun_a_one(self):
        x = 10
        a = 1
        expected_result = (x + 25) / 2
        result = gammafun(x, a)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_gammafun_large_a(self):
        x = 10
        a = 1e6
        expected_result = 24.9999850000
        result = gammafun(x, a)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_gammafun_negative_a(self):
        x = 10
        a = -1
        with self.assertRaises(ZeroDivisionError):
            gammafun(x, a)

    def test_gammafun_array_x(self):
        x = np.array([10, 20, 30])
        a = 1
        expected_result = (x + 25) / 2
        result = gammafun(x, a)
        np.testing.assert_array_almost_equal(result, expected_result, decimal=7)

if __name__ == '__main__':
    unittest.main()



