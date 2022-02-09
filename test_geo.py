"""Unit test for the Geo Module"""
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

stations = build_station_list()


def test_rivers_with_station():
    """test that rivers_with_station only returns each river once"""
    #turn the rivers_with_station set list  
    rivers_list = list(rivers_with_station(stations))  
    #create a set from that list which will have no duplicates  
    rivers_set = set(rivers_with_station(stations))
    #test if the lengh of the list and set are the same (if they are the same- no duplicate entries)
    assert len(rivers_list) == len(rivers_set)



def test_station_by_river(): 
    """test if station_by_river is callable"""
    x= station_by_river(stations)



def test_stations_by_distance():
    """Test whether stations_by_distance has the list ordered correctly"""
    
    listed_stations = stations_by_distance(stations)
    assert sorted_by_key(listed_stations, 1) == listed_stations
 
    stations_list = list(listed_stations)  
    stations_set = set(listed_stations)
    assert len(stations_set) == len(stations_list)



def test_rivers_by_station_number():
    """Test whether function output has a length greater than or equal to N"""
    
    stations_per_river = rivers_by_station_number(stations, 15)
    assert len(stations_per_river) >= 15

    rivers_list = list(stations_per_river)  
    rivers_set = set(stations_per_river)
    assert len(rivers_list) == len(rivers_set)



def test_stations_within_radius():
    """Test that the list contains no repeat values"""
    
    centre = (52.2053, 0.1218)
    r = 10
    stations_within_rds = stations_within_radius(stations, centre, r)

    rivers_list = list(stations_within_rds)  
    rivers_set = set(stations_within_rds)
    assert len(rivers_list) == len(rivers_set)