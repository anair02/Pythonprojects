from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
# Input x and y data
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([0.0025,0.005,0.0065,0.0095,0.0115,0.013,0.0155,0.0175,0.020,0.0225])
# Perform linear regression of the xy data 
# Print results
slope = stats.linregress(x, y)[0]
std_err = stats.linregress(x, y)[4]
intercept = stats.linregress(x, y)[1]
print ("slope = ", slope)
print ("standard error of the slope = ", std_err)
print ("intercept = ", intercept)
# Calculate the linear fit data
# with the calculated fit and intercept
# from linear regression
fit = intercept + slope * x
# Plot the xy data and the calculated fit
# on the same graph
# Annotate the plot
plt.plot(x, y, 'o')         # o:circle
plt.plot(x, fit, 'k-')      # k: black, -: line
plt.title('Radius vs. Velocity')
plt.legend(['Measured data','Fit'],loc=0)  #'loc=0: 'best location'
plt.xlabel('Radius (m)')
plt.ylabel('Velocity (10^6 m/s)')
plt.show()