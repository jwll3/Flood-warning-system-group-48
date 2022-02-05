# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from winreg import DeleteValue
from .utils import sorted_by_key  # noqa
import math


def stations_by_distance(stations, p):
    """Returns a list of tuples of stations and their distance from coordinate p, ordered by their distance from p"""

    list_of_stations_by_distance = []

    # Find the distance of each station from the coordinate p
    for i in range(len(stations)):
 
        # Haversine Formula
        phi_1 = p[0] *(math.pi/180)
        phi_2 = stations[i].coord[0] *(math.pi/180)
        delta_phi = (phi_1 - phi_2)
        delta_lambda = (p[1] - stations[i].coord[1])*(math.pi/180)

        a = (math.sin(delta_phi / 2))**2 + math.cos(phi_1) * math.cos(phi_2) * ((math.sin(delta_lambda / 2))**2)

        c = 2*math.atan2((a**(0.5)), ((1-a)**(0.5)))

        distance = 6371 * c

        ith_station = (stations[i], distance)

        # Appends station and distance to the list of stations and distances
        list_of_stations_by_distance.append(ith_station)


    # Sorts the list by their distances (second entry in tuple)
    sorted_list = sorted_by_key(list_of_stations_by_distance, 1)

    return sorted_list

    

        











def stations_within_radius(stations, centre, r):
    """returns a list of all stations (type MonitoringStation) within the radius r, of centrepoint coordinate x"""


from .utils import sorted_by_key  # noqa



# Task 1D also goes below in this section

def rivers_with_station(stations): 
    """"""





# Task 1E is down here:

def rivers_by_station_number(stations, N):