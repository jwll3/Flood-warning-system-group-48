from .datafetcher import fetch_measure_levels

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):


    # Fetch data over past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=timedelta(days=dt))

    # Print level history
    for date, level in zip(dates, levels):
        print(date, level)


    #dt = 2
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=timedelta(days=dt))

    # Print level history
    for date, level in zip(dates, levels):
        print(date, level)



    tt = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
        datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
        datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    # Plot
    plt.plot(tt, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station A")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()