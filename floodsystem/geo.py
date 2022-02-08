# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import haversine
from turtle import distance
def stations_by_distance(stations,p):
    """return a list of tuples containing stations and distances"""
    list0=[]
    for station in stations:
        coord=station.coord
        distance=haversine(p,coord)
        tuple0=(station.name,station.town,distance)
        list0+=tuple0
    return list0
         
