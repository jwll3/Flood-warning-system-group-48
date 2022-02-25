

import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
 

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
