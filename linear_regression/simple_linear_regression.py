import numpy as np
def slope_and_intercept(x, y):
    if x.ndim != 1:  # Optional check for 1D array
        raise ValueError("x array must be a 1D array.")
    if y.ndim != 1:  # Optional check for 1D array
        raise ValueError("y array must be a 1D array.")
    if np.size(x) != np.size(y):
        raise ValueError("The number of elements of x array and y array must be equal.")
    for i in x , y:
        xp = x-(np.mean(x)) 
        yp = y-(np.mean(y))
        # Calculates the slope
        slope = (np.sum((xp)*(yp))) / (np.sum((xp)**2))  
        # Calculates the intercept
        intercept = (np.mean(y)) - (slope *(np.mean(x)))
    
    return slope , intercept