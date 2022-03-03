import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
import datetime
from floodsystem.analysis import *
import numpy

# Build list of stations
stations = build_station_list()
update_water_levels(stations)


stations_list = stations_level_over_threshold(stations, 0.8)
selected_stations = stations_list[:5]

dt = 2
dt = datetime.timedelta(days=dt)


dates, levels = fetch_measure_levels(selected_stations[1][0].measure_id, dt)
station = selected_stations[1]



########################################################################################################################
# Create set of 10 data points on interval (1000, 1002)
def abacus(dates,levels,p):
    x = matplotlib.dates.date2num(dates)
    y = levels 

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    # Plot original data points
    #plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    #plt.plot(x1, poly(x1 - x[0]))

    return poly, d0 

    


def sucaba(station, dates, levels, p):

    # Create set of 10 data points on interval (1000, 1002)
    float_dates = matplotlib.dates.date2num(dates)
    x = np.linspace(float_dates[0], float_dates[-1], len(levels))
    y = levels 
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))
    station = station 
    # Display plot
    plt.xlabel('Time (over 2 days)')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station[0]) 
    
    plt.show()

    
"""
for i in range(len(selected_stations)):
    dates, levels = fetch_measure_levels(selected_stations[i][0].measure_id, dt)
    station = selected_stations[i]
    sucaba(station, dates, levels, 4)
"""
print (4)     
print(abacus(dates, levels, 4))
sucaba (station, dates, levels, 4)