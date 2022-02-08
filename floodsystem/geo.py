# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
pip install haversine
from turtle import distance
import haversine
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations,p):
    ''''''return a list of tuples containing stations and distances''''''
    list0=[]
    tuple0=(,)
    for i in range (len(stations)):
        tuple0[0]=stations[i].name
        coord=stations[i].coord
        distance=haversine(p,coord)
        tupe0[1]=distance
        list0+=tuple0
    return list0
         
def rivers_with_station(stations): #lists all rivers with monitoring stations and returns a dictionary
