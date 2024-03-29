# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


#from pandas import isnull

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.latest_level = None
    
    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """check if a station is inconsistent my returning false if there is either no typical range 
        or if the typical high range is less than the typical low """
        #check to see if there is a typical range
        if self.typical_range is None:
            return False 
        #check to see if typical high range is less than the typical low 
        elif self.typical_range[0] >= self.typical_range[1]: 
            return False 
        #otherwise fine 
        else: 
            return True

    def relative_water_level(self): 
        """Function that returns fraction of typical range, e.g. 1.0 for a typical high and 0.0 for a typical low"""
        #returns none if the typical range date is either missing or inconsistent 
        if (self.typical_range is None) or (self.latest_level is None):
            return None        
        elif self.typical_range[0] >= self.typical_range[1]: 
            return None        
        
        #if data is consistent, returns a fraction of typical range 
        else:
            #find the magnitude of the range 
            mag_range = self.typical_range[1] - self.typical_range[0]
            #finds the fraction from (latest level - typical low) / magnitude of range 
            water_level_fraction = (self.latest_level - self.typical_range[0]) / mag_range
        
            return water_level_fraction



def inconsistent_typical_range_stations(stations):
    """function that makes a list of inconsistent stations"""
    #list of inconsistent stations 
    inconsistent_stations = []
    #if a station is inconsistent (returning false from typical_range_consistent) then it is added to the list 
    for station in stations: 
        if MonitoringStation.typical_range_consistent(station) is False: 
            inconsistent_stations.append(station.name)   
        else: 
            pass 
    
    return inconsistent_stations


