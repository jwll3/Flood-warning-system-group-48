#from curses import KEY_A1
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
    
    #set up stations and dates for functions 
    stations_list = stations_level_over_threshold(stations, -1000)
    selected_stations = stations_list[0:200]
    dt = 2
    dt = datetime.timedelta(hours=dt)

    ##Create a list of tuples: station name and risk factor
    stations_risk_factor = []
    stations_risk_grading = []

    #this for loop is going to go through every station, and work out the rate of water level rise through backward differentiation
    #for i in range(len(valid_station_name_with_rel_level)):
    for i in range(len(selected_stations)):
        try:

            def find_rate_of_increase():
                #initial data needed for functions 
                dates, levels = fetch_measure_levels(selected_stations[i][0].measure_id, dt)
                station = selected_stations[i]

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
                #print (coefficients) 

                #extract just the coefficients of x^4, x^3 ect. from poly1d object 
                terms = coefficients[0]
                #ie terms[0]) is the constant 
                #ie terms[3] is the x^3 coefficient 

                #create a function for the model polynomial 
                def Polynomial_function(x):
                    return terms[4]*x*x*x*x + terms[3]*x*x*x + terms[2]*x*x + terms[1]*x + terms[0]
        
                #f(a)
                First_term = Polynomial_function(latest_time_on_graph)
                #f(a-h)
                Second_term = Polynomial_function(latest_time_on_graph-one_step_back)
                #h = one_step_back

                def Numerical_backward_differentiation( first, second, h): #value of h is size of step for backward differentiation
                    return ((first-second) / h) 

                rate_of_water_level_rise = Numerical_backward_differentiation (First_term, Second_term, one_step_back) # gives a value of rise in water level per day accoring to latest reading and the one right before it 

                #print(selected_stations[i][0].name)
                #print (rate_of_water_level_rise) 

                return rate_of_water_level_rise

            

            ##Calculate the risk factor and append to the list.
            K_1 = 10
            K_2 = 1

            #risk_factor = (K_1 * rate_of_water_level_rise) + (K_2 * selected_stations[i][0].relative_water_level())
            risk_grading = "Undetermined"

            ##Determine the risk gradings

            if selected_stations[i][0].relative_water_level() <= 0.8:
                risk_grading = "No Risk"
                


            elif (selected_stations[i][0].relative_water_level() > 0.8):
                rate_of_water_level_rise = find_rate_of_increase()
                water_level = selected_stations[i][0].relative_water_level()
                risk_factor = (K_1 * rate_of_water_level_rise) + (K_2 * water_level)

                #print(selected_stations[i][0].name)
                #print(rate_of_water_level_rise)
                #print(water_level)
                #print(risk_factor)

                if (risk_factor >= 10) and (rate_of_water_level_rise > 0):
                    risk_grading = "severe"

                elif (risk_factor >= 10) and (rate_of_water_level_rise < 0):
                    risk_grading = "high"

                elif (2 <= risk_factor <= 10) and (rate_of_water_level_rise > 0):
                    risk_grading = "high"

                elif (2 <= risk_factor <= 10) and (rate_of_water_level_rise < 0):
                    risk_grading = "moderate"

                elif (1.5 <= risk_factor <= 2) and (rate_of_water_level_rise > 0):
                    risk_grading = "moderate"

                elif (1.5 <= risk_factor <= 2) and (rate_of_water_level_rise < 0):
                    risk_grading = "low"

                elif (risk_factor <= 1.5) and (rate_of_water_level_rise > 0):
                    risk_grading = "low"

                elif (risk_factor <= 2) and (rate_of_water_level_rise < 0):
                    risk_grading = "No Risk"



            #factor_tuple_to_append = (selected_stations[i][0].name, risk_factor)
            #stations_risk_factor.append(factor_tuple_to_append)

            if risk_grading == "No Risk":
                pass
            else: 
                grading_tuple_to_append = (selected_stations[i][0].name, risk_grading)
                stations_risk_grading.append(grading_tuple_to_append)

            
            
            #print(stations_risk_factor)

            #plot_water_levels(selected_stations[i][0], dates, levels)

        except:
            pass
    
    print(stations_risk_grading)








if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

#test 
