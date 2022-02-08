# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from turtle import distance
from .utils import sorted_by_key  # noqa
def stations_by_distance(stations,p):
    """return a list of tuples containing stations and distances"""
    list0=[]
    tuple0=(0,0,0)
    for i in range (len(stations)):
        tuple0[0]=stations[i].name
        tuple0[1]=stations[i].town
        coord=stations[i].coord
        distance=haversine(p,coord)
        tuple0[2]=distance
        list0+=tuple0
    return list0
         
