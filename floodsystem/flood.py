"""This module provides tools for assessing the flood level

"""
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns list of tuples of the station object and its relative water level, in descending order"""
    list_to_return = []
    for station in stations:
        if station.relative_water_level() is None:
            pass
        elif station.relative_water_level() >= tol:
            new_tuple = (station, station.relative_water_level())
            list_to_return.append(new_tuple)

        else:
            pass

    return sorted_by_key(list_to_return, 1, reverse=True)


def stations_highest_rel_level(stations, N): 
   
    dictionary_of_stations_to_level = {}
    """
    for station in stations:
        #if (station.typical_range() is None):
        if station.typical_range_consistent() is False: 
            pass

        else:  
            dictionary_of_stations_to_level[station.relative_water_level()] += [station.relative_water_level()]
            #dictionary_of_stations_to_level[station.name()] += [station.relative_water_level()]   
        
    sort_dictionary_of_stations_to_level = sorted(dictionary_of_stations_to_level.items(), key=lambda x:x[1], reverse=True)
    #sort_dictionary_of_stations_to_level2 = sorted(dictionary_of_stations_to_level) 
    #return sort_dictionary_of_stations_to_level
    """
    for k in range(len(stations)):
        if stations[k].typical_range_consistent() is False:
            pass
        else:
            dictionary_of_stations_to_level[stations[k].name] += [stations[k].relative_water_level()]

    n=int(N)
    first_N_highest_rel_level = []
    sort_dictionary_of_stations_to_level = sorted(dictionary_of_stations_to_level.items(), key=lambda x:x[1], reverse=True)

    for i in range(n):
        first_N_highest_rel_level.append(sort_dictionary_of_stations_to_level(i[0],i[1]))

        
    return first_N_highest_rel_level


    #first_N_highest_rel_level = [] 
    #for i in range(n): 
    #    first_N_highest_rel_level.append(sort_dictionary_of_stations_to_level(i[0],i[1])) 

    #return first_N_highest_rel_level
  

    """
    dictionary_of_stations_to_level = {"test":1}
    test=()


    for k in range(len(stations)):
        if stations[k].typical_range_consistent() is False:
            pass
        else:
            dictionary_of_stations_to_level[station[k].name] += [station[k].relative_water_level()]
            #dictionary_of_stations_to_level ["test"] = [k] #[stations[k].name] = [stations[k].relative_water_level()] 

    return test

    """