#Submodule containing 2G flood warning assessment function

def warning(stations):
    levelList = list()
    severeList = list()
    for s in stations:
        level = ""
        if s.typical_range_consistent() == False or s.latest_level == None:
            level = "Inconclusive"
        elif s.relative_water_level > 1 and trend > 1: #update this once Leo's code arrives for trend calculations
            level = "Severe"
            severeList.append(s.name)
        elif s.relative_water_level > 1 or trend > 1: #update this once Leo's code arrive for trend calculations
            level = "High"
        elif s. relative_water_level > 0.7:
            level = "Moderate"
        else:
            level = "Low"
        levelList.append(s.name, s.relative_water_level, level)
    return severeList