
def stations_level_over_threshold(stations, tol): #2B part 2
    stationList = []
    for station in stations:
        if station.typical_range_consistent() and station.latest_level != None:
            if station.relative_water_level() > tol:
                stationList.append((station.name, station.relative_water_level()))
    sortedList = sorted(stationList, key=lambda x: x[1], reverse=True)
    return sortedList