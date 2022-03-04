from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
dt=2
num_stations=5
stations=build_station_list()
update_water_levels(stations)
def run():
     list_of_top5=stations_highest_rel_level(stations, 5)
     for i in list_of_top5:
         dates, levels = fetch_measure_levels(
             i[0].measure_id, dt=datetime.timedelta(days=dt))
         plot_water_level_with_fit(i[0],dates,levels,4)
         
         
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()