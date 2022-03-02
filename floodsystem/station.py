# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from sklearn.manifold import trustworthiness


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    def typical_range_consistent(self):
        """checks the typical high/low range data for consistency."""
        if self.typical_range ==  None:
            return False
        elif self.typical_range[1] > self.typical_range[0]:
            return True
        else:
            return False
    def relative_water_level(self):
        """returns current water level as percentage of typical range"""
        if self.typical_range_consistent():
            fraction = self.latest_level/self.typical_range[1]
            return fraction
        else:
            return None
def inconsistent_typical_range_stations(stations):
    """given a list of station objects, returns a list of stations that have inconsistent data."""
    
    list1=[]
    for station in stations:
        if station.typical_range_consistent() :
            continue
        list1.append(station.name)
    return list1
