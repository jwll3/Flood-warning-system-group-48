"""Unit test for the Geo Module"""
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

stations = build_station_list()


"""Tests for 1D"""
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
     
