from subprocess import list2cmdline
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key
def run():
    """"return a list of stations with 10km of CCambridge city centre"""
    centre_coord=(52.2053,0.1218)
    stations=build_station_list()
    r=10
    list2=[]
    list1=stations_within_radius(stations,centre_coord,r)
    for station in list1:
        list2+=station[0]
    list2.sort()
    return list2
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
