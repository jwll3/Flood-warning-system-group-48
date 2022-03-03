from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
import datetime
from floodsystem.analysis import polyfit
import numpy

 

def run():
    
    
    """Requirements for Task2F"""

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #set up stations and dates for functions 
    stations_list = stations_level_over_threshold(stations, 0)
    selected_stations = stations_list[:5]
    dt = 2
    dt = datetime.timedelta(days=dt)
    """
    #print values of poly and d0, as well as the graph for station 1
    letcomb brasset has no values so cannot plot a graph for this point 
    dates, levels = fetch_measure_levels(selected_stations[1][0].measure_id, dt)
    station = selected_stations[1]

    print("poly and d0 for:")
    print (str(station[0].name))
    print(polyfit(dates,levels,4))
    plot_water_level_with_fit(station, dates, levels, 4)
    """
    for i in range(5):
        dates, levels = fetch_measure_levels(selected_stations[i+1][0].measure_id, dt)
        station = selected_stations[i+1]

        print("poly and d0 for:")
        print (str(station[0].name))
        print(polyfit(dates,levels,4))
        plot_water_level_with_fit(station, dates, levels, 4)

    """
    #print values of poly and d0, as well as the graph for station 2 
    dates, levels = fetch_measure_levels(selected_stations[1][0].measure_id, dt)
    station = selected_stations[1]

    print("poly and d0 for:")
    print (str(station[0].name))
    print(polyfit(dates,levels,4))
    plot_water_level_with_fit(station, dates, levels, 4)

    #print values of poly and d0, as well as the graph for station 3 
    dates, levels = fetch_measure_levels(selected_stations[2][0].measure_id, dt)
    station = selected_stations[2]

    print("poly and d0 for:")
    print (str(station[0].name))
    print(polyfit(dates,levels,4))
    plot_water_level_with_fit(station, dates, levels, 4)

    #print values of poly and d0, as well as the graph for station 4 
    dates, levels = fetch_measure_levels(selected_stations[3][0].measure_id, dt)
    station = selected_stations[3]

    print("poly and d0 for:")
    print (str(station[0].name))
    print(polyfit(dates,levels,4))
    plot_water_level_with_fit(station, dates, levels, 4)

    #print values of poly and d0, as well as the graph for station 5 
    dates, levels = fetch_measure_levels(selected_stations[4][0].measure_id, dt)
    station = selected_stations[4]

    print("poly and d0 for:")
    print (str(station[0].name))
    print(polyfit(dates,levels,4))
    plot_water_level_with_fit(station, dates, levels, 4)
    """
    
        

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()