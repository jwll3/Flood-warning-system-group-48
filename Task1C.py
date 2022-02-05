from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    #Setting the value for centre coordinate and radius r
    centre = (52.2053, 0.1218)
    r = 10
    stations_within_required_radius = stations_within_radius(stations, centre, r)
    sorted_list = sorted(stations_within_required_radius)
    print(sorted(sorted_list))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()