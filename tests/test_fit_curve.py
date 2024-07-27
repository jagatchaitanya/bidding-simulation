import unittest
import numpy as np
from models.fit_curve import fit_curve
from models.model import gammafun

class TestFitCurveFunction(unittest.TestCase):

    def test_fit_curve_simple(self):
        x_data = np.array([0, 1, 2, 3, 4, 5])
        # Generate y_data using the gammafun with known parameter a=2
        y_data = gammafun(x_data, 2)
        
        # Fit the curve
        popt, pcov = fit_curve(x_data, y_data)
        
        # The parameter 'a' should be close to 2
        self.assertAlmostEqual(popt[0], 2, places=4)

    def test_fit_curve_noise(self):
        x_data = np.linspace(0, 5, 50)
        np.random.seed(0)
        # Generate y_data using the gammafun with known parameter a=2 and some added noise
        y_data = gammafun(x_data, 2) + np.random.normal(0, 0.5, size=x_data.shape)
        
        # Fit the curve
        popt, pcov = fit_curve(x_data, y_data)
        
        # The parameter 'a' should be close to 2 despite the noise
        self.assertAlmostEqual(popt[0], 2, places=1)

    def test_fit_curve_large_a(self):
        x_data = np.linspace(0, 5, 50)
        # Generate y_data using the gammafun with known parameter a=1e6
        y_data = gammafun(x_data, 1e6)
        
        # Fit the curve
        popt, pcov = fit_curve(x_data, y_data)
        
        # The parameter 'a' should be close to 1e6
        self.assertAlmostEqual(popt[0], 1e6, places=0)

    def test_fit_curve_negative_a(self):
        x_data = np.array([0, 1, 2, 3, 4, 5])
        # Generate y_data using the gammafun with known parameter a=-0.5
        y_data = gammafun(x_data, -0.5)
        
        # Fit the curve
        popt, pcov = fit_curve(x_data, y_data)
        
        # The parameter 'a' should be close to -0.5
        self.assertAlmostEqual(popt[0], -0.5, places=4)

if __name__ == '__main__':
    unittest.main()
