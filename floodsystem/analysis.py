import matplotlib
import numpy as np
import matplotlib.pyplot as plt
def polyfit(dates, levels, p):
    # convert dates to floats
    x = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x-x[0], levels, 4)

    # Convert coefficient into a polynomial that can be evaluated, 
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly