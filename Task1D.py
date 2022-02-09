# Demonstration program to show functionality of 1D functions

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
rivers = tuple(rivers)
rivers = sorted(rivers)
print("There are " + str(len(rivers)) + " rivers. First 10: " + str(rivers[-10:]))

riverStations = stations_by_river(stations)
print("River Aire: " + str(riverStations['River Aire']))
print("River Cam: " + str(riverStations['River Cam']))
print("River Thames: " + str(riverStations['River Thames']))