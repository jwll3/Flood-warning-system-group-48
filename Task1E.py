from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    # Choose a value for N:
    N = 9

    # Produce a list of tuples of river and number of stations
    river_and_num_stations = rivers_by_station_number(stations, N)

    print(river_and_num_stations)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()