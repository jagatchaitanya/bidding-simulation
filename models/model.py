import numpy as np

def gammafun(x, alpha):
    adash = 25
    return x*(1/(1+alpha)) + adash*(alpha/(1+alpha))
