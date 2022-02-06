from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

stations = build_station_list()

#print(rivers_with_station(stations))
print ("dictionary:")
print(station_by_river(stations)) 

