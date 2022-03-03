from floodsystem.analysis import *
from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime 
import numpy
from floodsystem.plot import *
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
import datetime
from floodsystem.analysis import polyfit


def test_polyfit():
     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #set up stations and dates for functions 
    stations_list = stations_level_over_threshold(stations, 0)
    selected_stations = stations_list#[:5]
    dt = 2
    dt = datetime.timedelta(days=dt)

    #test 3rd station 

    dates, levels = fetch_measure_levels(selected_stations[2][0].measure_id, dt)
    station = selected_stations[2]

    poly, d0 = polyfit(dates,levels,4)
    assert isinstance(poly, numpy.poly1d)
    assert isinstance(d0, float)
     