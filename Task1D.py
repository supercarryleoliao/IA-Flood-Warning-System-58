# Demonstration program to show functionality of 1D functions

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
rivers = tuple(rivers)
rivers = sorted(rivers, reverse=True)
print("There are " + str(len(rivers)) + " rivers. First 10: " + str(rivers[-10:]))

riverStations = stations_by_river(stations)
print("River Aire: " + str(sorted(riverStations['River Aire'])))
print("River Cam: " + str(sorted(riverStations['River Cam'])))
print("River Thames: " + str(sorted(riverStations['River Thames'])))