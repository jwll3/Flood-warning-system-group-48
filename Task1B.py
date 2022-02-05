
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance



def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    #Sets a value for the coordinate tuple p, in this case Cambridge city centre:
    p = (52.2053, 0.1218)

    # Order stations by distance:
    stations_ordered_by_distance = stations_by_distance(stations, p)
    station_town_distance = []
    for j in range(len(stations_ordered_by_distance)):
        jth_station = stations_ordered_by_distance[j]

        station_to_append = (jth_station[0].name, jth_station[0].town, jth_station[1])

        station_town_distance.append(station_to_append)
    
    print("10 Closest Stations: ")
    print(station_town_distance[:10])
    print("10 Furthest Stations: ")
    print(station_town_distance[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

