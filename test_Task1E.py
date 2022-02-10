from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list 
def test_Task1E():
    stations=build_station_list()
    rivers = rivers_by_station_number(stations, 9)
    assert rivers[0][1] == 55
    assert rivers[1][1] == 31
    assert rivers[2][1] == 30
    assert rivers[3][1] == 25
    assert rivers[4][1] == 24
    assert rivers[5][1] == 23
    assert rivers[6][1] == 21
    assert rivers[7][1] == 21
    assert rivers[8][1] == 18
    assert rivers[9][1] == 18
    assert len(rivers) == 10