from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()

def run():
    # Update latest level data for all stations
    update_water_levels(stations)
    
    #print(stations_level_over_threshold(stations, 0))
    print(stations_highest_rel_level(stations, 10)) 

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
