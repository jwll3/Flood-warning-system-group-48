from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.stationdata import build_station_list

stations= build_station_list()

#print(typical_range_consistent(self))

print(inconsistent_typical_range_stations(stations))

