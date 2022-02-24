"""This module provides tools for assessing the flood level

"""
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns list of tuples of the station object and its relative water level, in descending order, if the """
        
    
    list_to_return = []
    for station in stations:
        if (station.typical_range is None) or (station.latest_level is None):
            pass

        elif station.typical_range[0] >= station.typical_range[1]: 
            pass

        elif station.relative_water_level() >= tol:
            new_tuple = (station, station.relative_water_level())
            list_to_return.append(new_tuple)
                 
        else:
            pass

    return sorted_by_key(list_to_return, 1, reverse=True)


