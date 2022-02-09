from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key
import haversine
def run():
    """Requirements for Task 1B"""

     # Build list of stations
    stations = build_station_list()
    coord_of_Cambridgecitycentre=(52.2053,0.1218)

    list1=stations_by_distance(stations,coord_of_Cambridgecitycentre)
    list2=sorted_by_key(list1, 2,reverse=False)
    return list2

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()