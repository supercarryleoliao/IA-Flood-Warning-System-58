from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
def run():
    """Requirements for Task 1B"""

     # Build list of stations
    stations = build_station_list()
    coord_of_Cambridgecitycentre=(52.2053,0.1218)

    stations_by_distance(stations,coord_of_Cambridgecitycentre)