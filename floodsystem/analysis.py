import matplotlib
import numpy as np
import matplotlib.pyplot as plt
def polyfit(dates, levels, p):
    # convert dates to floats
    x = matplotlib.dates.date2num(dates)
    d0=x[0]
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x-x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated, 
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly,d0
def plot_water_level_with_fit(station, dates, levels, p):
    poly,d0=polyfit(dates, levels, p)
    typical_range=station.typical_range
    x = matplotlib.dates.date2num(dates)
    high_value=[typical_range[1]]*len(x)
    low_value=[typical_range[0]]*len(x)
    plt.plot(x,poly(x-d0),label="$polyfit line$")
    plt.plot(x,high_value,linestyle="dotted",color='r',label="$typical_high$")
    plt.plot(x,low_value,linestyle="dotted",color='g',label="$typical_low$")
    plt.title("Water levels of {}".format(station.name))
    plt.xlabel('dates')
    plt.ylabel('levels')
    plt.legend()
    plt.show()