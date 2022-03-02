from floodsystem.stationdata import build_station_list
from Task2B import run 
def test_Task2B():
    testList = run()
    assert testList[0][1] > testList[-1][1]
    assert testList[-1][1] > 0.8