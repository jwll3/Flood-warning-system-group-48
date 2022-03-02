import matplotlib
import numpy as np
import matplotlib.pyplot as plt




def polyfit(dates,levels,p):
    float_dates = matplotlib.dates.date2num(dates)
    
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(float_dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(dates, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(dates[0], dates[-1], 30)
    #plt.plot(x1, poly(x1 - dates[0]))

    # Display plot
    #plt.show()

    return poly, x1 
    






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


