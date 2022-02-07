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
    """Returns a list of all stations (type MonitoringStation) within the radius r, of centrepoint coordinate x"""

    # Uses the function from exercise B to create a list of tuples of stations and distance from the coordinate
    stations_distance_from_coord = stations_by_distance(stations, centre)
    list_required = []
    for entry in stations_distance_from_coord:
        if entry[1] <= r:
            list_required.append(entry[0].name)
        else:
            pass
    return list_required








# Task 1D also goes below in this section

def rivers_with_station(stations): 
    """Returns the names of rivers with a monitoring station, from MonitorStation """
    #put rivers into a set, so repeat entries are removed 
    rivers = set()
    for k in range(len(stations)):
        rivers.add(stations[k].river) 
    return rivers 

def station_by_river(stations): 
    """creates a dictionary for each river and its coresponding stations"""
    #creating a dictionary                                                                 
    stations_to_river_dict = {}

    for k in range(len(stations)):
        #if the stations river is already in the dictionary, only append the name of the station
        if stations[k].river in stations_to_river_dict:
            stations_to_river_dict[stations[k].river].append(stations[k].name)
        #otherwise, the river is yet in the dictionary, so append both to the dictionary      
        else: 
            stations_to_river_dict[stations[k].river] = [stations[k].name]
    return stations_to_river_dict




# Task 1E is down here:

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring stations"""

    # Form a list of river names
    river_names_list = []
    for i in range(len(stations)):
        river_names_list.append(stations[i].river)

    # Form the list of tuples
    list_of_tuples = []

    for j in range(len(river_names_list)):
        jth_river = river_names_list[j]

        jth_counter = 0
        for k in range(len(river_names_list)):
            if jth_river == river_names_list[k]:
                jth_counter = jth_counter + 1
            else:
                pass

        new_tuple = (jth_river, jth_counter)
        list_of_tuples.append(new_tuple)

    # Remove repeats
    list_of_tuples_no_repeats = []
    for m in range(len(list_of_tuples)):
        if list_of_tuples[m] in list_of_tuples_no_repeats:
            pass
        else:
            list_of_tuples_no_repeats.append(list_of_tuples[m])

        # Order the List by number of stations
    ordered_list = sorted_by_key(list_of_tuples_no_repeats, 1, True)

    #Create a list for the first N entries:
    new_list = ordered_list[:N]

    # If the Nth entry has the same number of stations as the (N+1)th station etc, then include it in the list
    carry_on = True
    z = 1
    while carry_on == True:
        if new_list[N-1][1] == ordered_list[N+z-1][1]:
            new_list.append(ordered_list[N-z+1])
            z = z+1
        else: carry_on = False

    return new_list
