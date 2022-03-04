# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides interface for extracting statiob data from
JSON objects fetched from the Internet and

"""
import matplotlib
from . import datafetcher
from .station import MonitoringStation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def build_station_list(use_cache=True):
    """Build and return a list of all river level monitoring stations
    based on data fetched from the Environment agency. Each station is
    represented as a MonitoringStation object.

    The available data for some station is incomplete or not
    available.

    """

    # Fetch station data
    data = datafetcher.fetch_station_data(use_cache)

    # Build list of MonitoringStation objects
    stations = []
    for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']

        # Extract river name (not always available)
        river = None
        if 'riverName' in e:
            river = e['riverName']

        # Attempt to extract typical range (low, high)
        try:
            typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))
        except Exception:
            typical_range = None

        try:
            # Create mesure station object if all required data is
            # available, and add to list
            s = MonitoringStation(
                station_id=e['@id'],
                measure_id=e['measures'][-1]['@id'],
                label=e['label'],
                coord=(float(e['lat']), float(e['long'])),
                typical_range=typical_range,
                river=river,
                town=town)
            stations.append(s)
        except Exception:
            # Not all required data on the station was available, so
            # skip over
            pass

    return stations


def update_water_levels(stations):
    """Attach level data contained in measure_data to stations"""

    # Fetch level data
    measure_data = datafetcher.fetch_latest_water_level_data()

    # Build map from measure id to latest reading (value)
    measure_id_to_value = dict()
    for measure in measure_data['items']:
        if 'latestReading' in measure:
            latest_reading = measure['latestReading']
            measure_id = latest_reading['measure']
            measure_id_to_value[measure_id] = latest_reading['value']

    # Attach latest reading to station objects
    for station in stations:

        # Reset latestlevel
        station.latest_level = None

        # Atach new level data (if available)
        if station.measure_id in measure_id_to_value:
            if isinstance(measure_id_to_value[station.measure_id], float):
                station.latest_level = measure_id_to_value[station.measure_id]
def plot_water_levels(station, dates, levels):
    """ displays a plot (using Matplotlib) of the water level data against time for a station, and include on the plot lines for the typical low and high levels. """
    name=station.name
    typical_range=station.typical_range
    # Plot
    plt.plot(dates, levels)
    x = matplotlib.dates.date2num(dates)
    high_value=[typical_range[1]]*len(x)
    low_value=[typical_range[0]]*len(x)
    print(low_value)
    plt.plot(x,high_value,linestyle="dotted",color='r',label="$typical_high$")
    plt.plot(x,low_value,linestyle="dotted",color='g',label="$typical_low$")
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
