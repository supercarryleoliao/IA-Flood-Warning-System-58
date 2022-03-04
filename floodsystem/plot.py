import matplotlib
from .analysis import polyfit
import matplotlib.pyplot as plt
def plot_water_level_with_fit(station, dates, levels, p):
    poly,d0=polyfit(dates, levels, p)
    typical_range=station.typical_range
    x = matplotlib.dates.date2num(dates)
    high_value=typical_range[1]*len(x-d0)
    low_value=typical_range[0]*len(x-d0)
    plt.plot(x-d0,poly(x-d0),label="$polyfit line$")
    plt.plot(x-d0,high_value,linestyle="dotted",color='r',label="$typical_high$")
    plt.plot(x-d0,low_value,linestyle="dotted",color='g',label="$typical_low$")
    plt.xlabel('dates')
    plt.ylabel('levels')
    plt.legend()
    plt.show()