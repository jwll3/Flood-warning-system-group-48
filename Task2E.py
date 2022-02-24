from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels

def run():
    """Requirements for Task2E"""
    # Build list of stations
    stations = build_station_list()

    # Station name to find
    station_name = "Cam"


    plot_water_levels(stations[0], 3, 5)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
