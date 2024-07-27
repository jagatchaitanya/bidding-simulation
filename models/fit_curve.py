from scipy.optimize import curve_fit
from models.model import gammafun

def fit_curve(x_data, y_data):
    popt, pcov = curve_fit(gammafun, x_data, y_data)
    return popt, pcov