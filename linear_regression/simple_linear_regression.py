import numpy as np
def slope_and_intercept(x, y):
    """
    Calculate the slope and intercept

    Parameters
    ------
    x (array_like): 1D array
    y (array_like): 1D array

    Returns
    ------
    slope (float): The line slope in simple linear regression.
    intercept (float): Constant value in simple linear regression.

    Raises
    ------
    ValueError: If the number of elements of x array and y array is equal.

    Exampls
    ------
    >>> import numpy as np
    >>> x = np.array([1, 2, 4 ,6 ,8 ,3, 9])
    >>> y = np.array([10, 2, 6, 5, 12, 7, 12])
    >>> slope , intercept = slope_and_intercept(x, y)
    >>> slope
    0.6932989690721649
    >>> intercept
    4.445876288659794

    ------

    >>> import numpy as np
    >>> x = np.array([1, 2])
    >>> y = np.array([3, 4])
    >>> slope , intercept = slope_and_intercept(x, y)
    >>> slope
    1.0
    >>> intercept
    2.0

    ------
    >>> import numpy as np
    >>> x = np.array([1, 2])
    >>> y = np.array([3, 4, 7])
    >>> slope , intercept = slope_and_intercept(x, y)
    Traceback (most recent call last):
        raise ValueError("The number of elements of x array and y array must be equal.")
  
    """
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