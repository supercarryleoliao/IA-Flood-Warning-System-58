from floodsystem.stationdata import build_station_list
from Task2C import run 
def test_Task2C():
    testList = run()
    assert len(testList) == 10
    assert testList[0][1] > testList[-1][1]