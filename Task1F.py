from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
def run():
    """"return a list of station names, in alphabetical order, for stations with inconsistent data"""
    stations=build_station_list()
    list1=inconsistent_typical_range_stations(stations)
    list1.sort()
    return list1
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()