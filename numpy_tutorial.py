"""
    Numpy or Numerical python is a third party python library used ...
    I am learning it Yeah...Finally...
    command to install it :
    1-> On GNU/Mac:    python3 -m pip install numpy 
    2-> On Windows : pip install numpy
    To use the functionalities of the numpy library firstly we need to import it using 'import numpy' statement.
"""
import numpy as np      # importing numpy as np (an alias)

# creating a numpy array
array_1 = np.array([1,2,3,4,5,6],ndmin=1)
print(array_1)

# finding  the maximum element out of the array
print(np.max(array_1))

# finding the minmmum element of the array
print(np.min(array_1))

# finding the mean of the array
print(np.mean(array_1))

# finding the median of the array 
print(np.median(array_1))

# finding the variance of the array 
print(np.var(array_1))

# finding the standard deviation of the array
print(np.std(array_1))