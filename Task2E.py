from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
import datetime

def run():
    """Requirements for Task2E"""
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)


    stations_list = stations_level_over_threshold(stations, 0.8)
    selected_stations = stations_list[:5]

    dt = 10
    dt = datetime.timedelta(days=dt)

    counter = 0
    for thing in selected_stations:
        dates, levels = fetch_measure_levels(selected_stations[counter][0].measure_id, dt)
        plot_water_levels(selected_stations[counter][0], dates, levels)
        counter = counter + 1


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()