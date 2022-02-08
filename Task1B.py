from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key
def run():
    """Requirements for Task 1B"""

     # Build list of stations
    stations = build_station_list()
    coord_of_Cambridgecitycentre=(52.2053,0.1218)

    list1=stations_by_distance(stations,coord_of_Cambridgecitycentre)
    sorted_by_key(list1, 2)
    return list1

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()