from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

stations = build_station_list()

#print(rivers_with_station(stations))
#print ("dictionary:")
#print(station_by_river(stations)) 


no_of_stations_with_river = len(rivers_with_station(stations))
rivers_list = list(rivers_with_station(stations))
alphabetical_rivers = sorted(rivers_list) 
print("test ")
print(alphabetical_rivers)

