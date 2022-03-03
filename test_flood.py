from  floodsystem.flood import *
from floodsystem.station import *
from floodsystem.stationdata import build_station_list

def test_stations_level_over_threshold():

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
    
    s.latest_level = 3.4445

    station_list = [s]

    assert len(stations_level_over_threshold(station_list, 0.9))==1

    