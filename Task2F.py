from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
import datetime
from floodsystem.analysis import polyfit
import numpy

 

def run():
    
    
    """Requirements for Task2F"""
    """
    stations = build_station_list()
    update_water_levels(stations)
    stations_list = stations_level_over_threshold(stations, 0.8)
    selected_stations = stations_list[:5]
    dt = 2
    dt = datetime.timedelta(days=dt)
    
    
    for thing in selected_stations:
        dates, levels = fetch_measure_levels(selected_stations[counter][0].measure_id, dt)
        plot_water_level_with_fit(selected_stations[counter][0],dates,levels,4)
        counter = counter + 1
    """

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)


    stations_list = stations_level_over_threshold(stations, 0)
    selected_stations = stations_list[:5]
    dt = 2
    dt = datetime.timedelta(days=dt)

    
    dates, levels = fetch_measure_levels(selected_stations[1][0].measure_id, dt)
    station = selected_stations[1]


    print("poly and d0 for")
    print(polyfit(dates,levels,4))
    plot_water_level_with_fit(station, dates, levels, 4)
        

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()