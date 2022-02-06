from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

stations = build_station_list()


def run():
    """Requirements for Task 1D"""

    """Part 1
    Print how many rivers have at least one monitoring station, and then list the first 10 in alphabetical order"""
    #find out how many rivers have at least one monitoring system 
    no_of_stations_with_river = len(rivers_with_station(stations))

    #turn the rivers_with_station set into a list so that it can be sorted 
    rivers_list = list(rivers_with_station(stations))
    #sorting the list of rivers alphabetically 
    alphabetical_rivers = sorted(rivers_list) 

    #printing the number of stations with a river 
    print("Number of rivers with at least one monitoring system: " + str(no_of_stations_with_river))

    #printing the first 10 rivers alphabetically 
    print ("First 10 rivers in alphbetical order:")
    print(alphabetical_rivers[:10])

    """Part 2
    Print the names of the stations located on the River Aire, Cam and Thames rivers in alphabetical order"""
    #output of station_by_river
    dictionary_of_rivers= station_by_river(stations)

    #function to sort the stations from a specified river alphabetically 
    def river_stations(wanted_river):
        #turning the stations form a specified river into a list  
        list_dictionary_of_rivers = list(dictionary_of_rivers[str(wanted_river)])
        #sorting the list 
        return(sorted(list_dictionary_of_rivers))   

    #printing the alphabetical stations from River Aire 
    print ("River Aire:")
    print (river_stations("River Aire")) 

    #printing the alphabetical stations from River Cam 
    print ("River Cam:")
    print (river_stations("River Cam")) 

    #printing the alphabetical stations from River Thames 
    print ("River Thames:")
    print (river_stations("River Thames")) 

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()