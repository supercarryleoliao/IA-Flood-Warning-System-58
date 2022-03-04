from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
dt=2
num_stations=5
stations=build_station_list()
def run():
     list_of_top5=stations_highest_rel_level(stations, 5)
     for i in list_of_top5:
         dates, levels = fetch_measure_levels(
             i.measure_id, dt=datetime.timedelta(days=dt))
         print (ployfit(dates,levels,4))
         print("check")
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()