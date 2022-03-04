#Demonstration program to show completeness of Task 2C
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
def run():
    stations = build_station_list()
    update_water_levels(stations)
    returnList = stations_highest_rel_level(stations, 10)
    list1=[]
    for i in returnList:
        list1.append((i[0].name,i[1]))
    return list1

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    x = run()
    print(x)