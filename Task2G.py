from floodsystem.stationdata import *
from floodsystem.analysis import *
from floodsystem.flood import *
from floodsystem.geo import* 
from floodsystem.plot import *
from floodsystem.station import* 
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    """Requirements for Task2G"""
    #add list of stations and update water levels 
    stations = build_station_list()
    update_water_levels(stations)
    
    #calculate the total number of consistent stations 
    Number_of_consistent_stations = len(stations) - len(inconsistent_typical_range_stations(stations))

    #print(stations_level_over_threshold(stations, 0)) 
    All_valid_stations = stations_level_over_threshold(stations, -1000)

    #valid stations name with relative water level 
    valid_station_name_with_rel_level = stations_highest_rel_level(stations, len(All_valid_stations)-200) 
    print (valid_station_name_with_rel_level)
    print (len(valid_station_name_with_rel_level))

    "ABOVE IS A REALLY BODGED WAY TO GET A LIST OF ALL STATIONS ALONG WITH THEIR RELATIVE LEVEL IN A LIST OF TUPLES. "
    "IT WOULD BE GOOD IF YOU COULD FIND A BETTER SYSTEM THAT DIDNT USE A -66 AT THE END TO REACH THE LIMIT"

    #set up stations and dates for functions 
    stations_list = stations_level_over_threshold(stations, -1000)
    selected_stations = stations_list
    dt = 2
    dt = datetime.timedelta(days=dt)



    "this bit works!"
    #this for loop is going to go through every station, and work out the rate of water level rise through backward integration
    #for i in range(len(valid_station_name_with_rel_level)):
    for i in range(len(100)):
        try:
            #initial data needed for functions 
            dates, levels = fetch_measure_levels(selected_stations[i+1][0].measure_id, dt)
            station = selected_stations[i+1]

            #turn dates into numerical values 
            float_dates = matplotlib.dates.date2num(dates)
            t = np.linspace(float_dates[0], float_dates[-1], len(levels))
            #Find the time of latest reading and the one before that, accounting for shift to avoid "poorly conditioned warnings"
            latest_time_on_graph = t[-1] -t[0]
            one_step_back = (t[-1] -t[0]) - (t[-2]-t[0]) 
            #two_step_back = (t[-1] -t[0]) - (t[-3] -t[0]) for example if you wanted a larger step back 
            # arbitary step of 1 is one day 
            #one step back is equivelent to rate in water level increase between this reading and the last 
        
            #work out the polyfit poly1d object for the polynomial 
            coefficients = polyfit(dates,levels,4)
            print (coefficients) 

            #extract just the coefficients of x^4, x^3 ect. from poly1d object 
            terms = coefficients[0]
            #ie terms[0]) is the constant 
            #ie terms[3] is the x^3 coefficient 

            #create a function for the model polynomial 
            def Polynomial_function(x):
                return terms[4]*x*x*x*x + terms[3]*x*x*x + terms[2]*x*x + terms[1]*x + terms[0]
    

            "For numerical backwards integration : (f(a) - f(a - h))/h, where f is polynomial function, a is latest_time_on_graph and h is one_step_back"

            #f(a)
            First_term = Polynomial_function(latest_time_on_graph)
        
            #f(a-h)
            Second_term = Polynomial_function(latest_time_on_graph-one_step_back)
        
            #h = one_step_back

            def Numerical_backward_integration( first, second, h): #value of h is size of step for backward integration
                return ((first-second) / h) 

            rate_of_water_level_rise = Numerical_backward_integration (First_term, Second_term, one_step_back) # gives a value of rise in water level per day accoring to latest reading and the one right before it 

            print (rate_of_water_level_rise) 

            "can you put water level rise into the tuple of the station"
            "i.e so you have [(station name, rel water level, rate of water level rise) (station name, rel water level, rate of water level rise)...]" 
            "sorry, would have done this bit myself but i couldnt figure out how to get all teh stations into the list (i have a bodged attemp above) "

        except:
            pass




if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

#test 