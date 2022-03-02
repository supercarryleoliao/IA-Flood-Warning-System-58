#Demonstration program to show completion of Task 2B
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
def run():
    stations = build_station_list()
    update_water_levels(stations)
    return stations_level_over_threshold(stations, 0.8)

if __name__ == "__main__":
    x = run()
    print(x)