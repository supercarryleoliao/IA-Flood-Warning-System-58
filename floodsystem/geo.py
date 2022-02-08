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
        if i['river'] not in stationList:
            stationList += i['river']
    return stationList