#Demonstration program to show completeness of Task 2C
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
def run():
    stations = build_station_list()
    update_water_levels(stations)
    returnList = stations_highest_rel_level(stations, 10)
    return returnList

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    x = run()
    print(x)