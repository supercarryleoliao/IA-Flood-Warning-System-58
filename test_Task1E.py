from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list 
def test_Task1E():
    stations=build_station_list()
    assert rivers_by_station_number(stations, 9) == [('River Thames', 55), ('River Avon', 31), ('River Great Ouse', 30), ('River Derwent', 25), ('River Aire', 24), ('River Calder', 23), ('River Stour', 21), ('River Severn', 21), ('River Colne', 18), ('River Ouse', 18)]