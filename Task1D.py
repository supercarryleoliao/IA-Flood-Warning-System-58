# Demonstration program to show functionality of 1D functions

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
rivers.sort()
print(len(rivers) + " stations. First 10: " + rivers[-10:])

riverStations = stations_by_river(stations)
print("River Aire: " + riverStations['River Aire'])
print("River Cam: " + riverStations['River Cam'])
print("River Thames: " + riverStations['River Thames'])