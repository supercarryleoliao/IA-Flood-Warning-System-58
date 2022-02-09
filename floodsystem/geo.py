# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from turtle import distance
import haversine
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations,p):
    #return a list of tuples containing stations and distances
    list0=[]
    for station in stations:
        coord=station.coord
        distance=haversine(p,coord)
        tuple0=(station.name,station.town,distance)
        list0+=tuple0
    return list0
def stations_within_radius(stations, centre, r):
    """"return a list of stations within radius r"""
    list1=[]
    for station in stations:
        if haversine(centre,station.coord) <= r:
            list1+=station
    return list1

         
def rivers_with_station(stations): #lists all rivers with monitoring stations
    stationList = set()
    for i in stations:
        stationList.add(i.river)
    return stationList

def stations_by_river(stations): #returns dictionary using river name as key and list of stations
    riverDict = dict()
    for river in rivers_with_station(stations):
        stationList = list()
        for i in stations:
            if i.river == river:
                stationList.append(i.name)
        riverDict[river] = stationList
    return riverDict

def rivers_by_station_number(stations, N):
    numberList = list()
    rivers = stations_by_river(stations)
    for r in rivers:
        numberList.append(tuple(r, len(rivers[r])))
    sortedList = sorted(numberList, key=lambda x: x[1])
    firstN = list()
    valueN = sortedList[N-1, 1]
    for x in sortedList:
        if x[1] <= valueN:
            firstN.append(x)
        else:
            break
    return firstN