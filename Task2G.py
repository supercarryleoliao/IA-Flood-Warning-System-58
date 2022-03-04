from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
def run():
    stations = build_station_list()
    update_water_levels(stations)
    returnList=stations_level_over_threshold(stations, 0.8)
    list_of_severe=[]
    list_of_high=[]
    list_of_moderate=[]
    list_of_low=[]
    for i in returnList:
        if i[1] > 3:
            list_of_severe.append(i[0].name)
        elif i[1] > 2:
            list_of_high.append(i[0].name)
        elif i[1] >1:
            list_of_moderate.append(i[0].name)
        elif i[1] > 0.8:
            list_of_low.append(i[0].name)
    print("list of station at severe risk: {}".format(list_of_severe))
    print("list of station at high risk: {}".format(list_of_high))
    print("list of station at moderate risk: {}".format(list_of_moderate))
    print("list of station at low risk: {}".format(list_of_low))
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()