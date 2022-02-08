# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

stations= build_station_list()


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

#tests for 1F 

def test_typical_range_consistent():
    """applying 2 test stations to see if function will correctly identify the consistent and inconsistent one"""
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    #made up station has consistent typical range value 
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    
    # Create another station 
    R_id = "test-R-id"
    T_id = "test-T-id"
    Rlabel = "some station"
    Rcoord = (-2.0, 4.0)
    #made up station has inconsistent typical range value (typical high range is less than the typical low)
    Rtrange = (3.4445, -2.3)
    Rriver = "River X"
    Rtown = "My Town"
    r = MonitoringStation(R_id, T_id, Rlabel, Rcoord, Rtrange, Rriver, Rtown)
    
    
    assert MonitoringStation.typical_range_consistent(s) is True 
    assert MonitoringStation.typical_range_consistent(r) is False


def test_inconsistent_typical_range_stations():
    """test that there are fewer inconsistent stations than total stations"""
    list_of_inconsistent_stations = inconsistent_typical_range_stations(stations)
    assert len(list_of_inconsistent_stations) < len(stations)

    """assert that every station in list_of_inconsistent_stations returens false"""
    for station in list_of_inconsistent_stations:
        assert MonitoringStation.typical_range_consistent(station) is False 
    
    
    """
    for i in range(len(list_of_inconsistent_stations)):
        assert MonitoringStation.typical_range_consistent(list_of_inconsistent_stations[i]) is False 
    """
    
