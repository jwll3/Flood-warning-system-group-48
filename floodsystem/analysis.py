import matplotlib
import numpy as np
import matplotlib.pyplot as plt



def polyfit(dates,levels,p):
    "returns d0, which is the shift applied to time axis to stop porly conditioned warnings"
    "and also returns poly, which gives the coefficients to a polynomial of best fit for levels against time"
    x = matplotlib.dates.date2num(dates)
    y = levels 

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    d0 = x[0]

    return poly, d0 
    
    """
    x = matplotlib.dates.date2num(dates)
    y = levels 

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    # Plot original data points
    #plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    #plt.plot(x1, poly(x1 - x[0]))

    return poly, d0 
    """

"""

def polyfit(dates,levels,p):
    x = matplotlib.dates.date2num(dates)
    
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x-x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(dates, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    #plt.plot(x1, poly(x1 - dates[0]))

    return poly, x1 
    
"""



"""

# Create set of 10 data points on interval (0, 2)
x = np.linspace(0, 2, 10)
y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

# Find coefficients of best-fit polynomial f(x) of degree 4
p_coeff = np.polyfit(x, y, 4)

# Convert coefficient into a polynomial that can be evaluated,
# e.g. poly(0.3)
poly = np.poly1d(p_coeff)

# Plot original data points
plt.plot(x, y, '.')

# Plot polynomial fit at 30 points along interval
x1 = np.linspace(x[0], x[-1], 30)
plt.plot(x1, poly(x1))

# Display plot
plt.show()

"""
