"""This module provides tools for assessing the flood level

"""
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns list of tuples of the station object and its relative water level, in descending order, if the """
    list_to_return = []
    for station in stations:
        if station.relative_water_level() >= tol:
            new_tuple = (station, station.relative_water_level())
            list_to_return.append(new_tuple)

        else:
            pass

    return list_to_return


