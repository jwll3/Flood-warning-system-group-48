from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.stationdata import build_station_list

stations= build_station_list()


def run():
    """Requirements for Task 1F"""
    list_of_inconsistent_stations = inconsistent_typical_range_stations(stations)
    #sort the list alphabetically, and then print 
    print (sorted(list_of_inconsistent_stations))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
