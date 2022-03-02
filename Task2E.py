import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
dt=10
num_stations=6
def run():
     list_of_top5=stations_highest_rel_level(stations, 5)
     for i in list_of_top5:
         dates, levels = fetch_measure_levels(
             i.measure_id, dt=datetime.timedelta(days=dt))
         plot_water_levels(i.name,dates,levels)
        
