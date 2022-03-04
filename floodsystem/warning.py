#Submodule containing 2G flood warning assessment function
import matplotlib
from scipy.misc import derivative
import numpy as np
from datetime import date

def trend(poly, d0):
    return derivative(poly, matplotlib.dates.date2num(date.today()))

def warning(stations):
    levelList = list()
    severeList = list()
    for s in stations:
        level = ""
        if s.typical_range_consistent() == False or s.latest_level == None:
            level = "Inconclusive"
        elif s.relative_water_level > 1 and trend(polyfit(dates, levels, 4)) > 0: #updated
            level = "Severe"
            severeList.append(s.town)
        elif s.relative_water_level > 1 or trend(polyfit(dates, levels, 4)) > 0: #updated
            level = "High"
        elif s.relative_water_level > 0.8:
            level = "Moderate"
        else:
            level = "Low"
        levelList.append(s.town, s.relative_water_level, level)
    return severeList