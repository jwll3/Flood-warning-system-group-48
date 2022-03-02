
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def plot_water_levels(station, dates, levels):
    """Returns a list of tuples with the station and relative water level"""

    highs = []
    lows = []

    if (station.typical_range is None):
        pass

    else:
        for i in range(len(levels)):
            highs.append(station.typical_range[1])
    
        plt.plot(dates, highs, label="Typical high level")

        for i in range(len(levels)):
            lows.append(station.typical_range[0])
    
        plt.plot(dates, lows, label="Typical low level")


    # Plot
    plt.plot(dates, levels)
    

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()



def plot_water_level_with_fit(station, dates, levels, p): 

    float_dates = matplotlib.dates.date2num(dates)
    
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(float_dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(dates, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))

    # Display plot
    print ("this is the graph of" + str(station.name))
    plt.show()
