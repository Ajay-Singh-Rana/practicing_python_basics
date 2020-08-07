# k@mlesh
# h3avren
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
print("array_1 = ",array_1,"\n")

# accessing elements of a numpy array
"""It is similar to the lists,we need to specify the element number-1 in the square brackets after the array name i.e. array[0] to access the first element"""
number  = array_1[3]    # a  value of 4 is assigned to the variable named number
print("4th element of array_1 is ",number,"\n")

# slicing a multidimensional  array
"""
Syntax:
    array_name[row_number_to_start_at:column_number_to_end_before,element_to_start_from:element_end_before]
"""
multiDimensional  = np.array([[12,13,14,15],[16,17,18,19],[20,21,22,23]])
print("Sliced array : ",multiDimensional[0:2,2:],"\n") # gets [[14,15],[18,19]]

# checking the shape of the array
"""The shape of the array is defined as (m,n) where m is the number of rows and n is the number of columns in the array"""
print("Shape of array_1 is ",array_1.shape,"\n")

# checking the size of the array
"""Size means the toatal number of elements in the array"""
print("Size of array_1 is ",array_1.size,"\n")

# checking the byte-size of the array i.e. number of bytes occupied in memory by each element
print("Memory size occupied by each element of array_1 is ",array_1.itemsize,"\n")

# adding analogous elements of two or more arrays
array_2 = np.array([7,8,9,10,11,12])
print("Sum of parallel array elements : ",array_1 + array_2,"\n")

# subtraction between analogous elements of two arrays
print("Difference of parallel array elements : ",array_2 - array_1,"\n")

# multiplication of analogous elements
print("Product of analogous array elements : ",array_1 * array_2,"\n")

# division between analogous elements
print("Distribution of analogous array elements : ",array_2 / array_1,"\n")

# sum of all the array elements
print("Sum of all array elements : ",np.sum(array_2),"\n")

# sum of the elements in a row
print("Sum of row-wise elements : ",np.sum(multiDimensional,axis=1),"\n")
# sum of the elements in a column
print("Sum of column-wise elements : ",np.sum(multiDimensional,axis=0),"\n")

# finding  the maximum element out of the array
print("Maximum : ",np.max(array_1),"\n")

# finding the minmmum element of the array
print("Minimum : ",np.min(array_1),"\n")

# finding the mean of the array
print("Mean : ",np.mean(array_1),"\n")

# finding the median of the array 
print("Median : ",np.median(array_1),"\n")

# finding the variance of the array 
print("Variance : ",np.var(array_1),"\n")

# finding the standard deviation of the array
print("Standard Deviation : ",np.std(array_1),"\n")

# reshaping an array
array_3 = multiDimensional.reshape(4,3)
print("Array before reshaping : ",multiDimensional,"\n")
print("Array after being reshaped : ",array_3,"\n")

# creating a linspace array
"""a linspace aaray or line-spaced array is the array of n equidistant numbers falling between two start and end points/numbers"""
array_4 = np.linspace(1,10,20)
print("Line-spaced array : ",array_4,"\n")

# finding square root of all elements of the array
array_5 = np.sqrt(array_4)
print("Square-roots of array elements : ",array_5,"\n")

# populating an array with numbers in a given range
array_6 = np.arange(17)
print("Array populated with arange() method : ",array_6,"\n")

# finding the data types of the array elements
print("Data-type of array elements : ",array_6.dtype,"\n")

# knowing the dimensions of the array
print("Dimensions of the array : ",array_6.ndim,"\n")

# concatenating two arrays 
print("Array concatenation/appending : ",np.hstack((array_1,array_2)),"\n")

# stacking two arrays 
print("Array stacking (vertical appending) : ",np.vstack((array_1,array_2)),"\n")

# converting an multidimensional array into a single dimensional array
print("Multi-dimensional array : ",multiDimensional,"\n")
print("Multi-dimensional array turned into a single dimensional array: ",np.ravel(multiDimensional),"\n")

# finding the natural log values of the array elements
print("Natural log of array elements : ",np.log(array_1),"\n")

# finding the log with base 10 values for all array elements
print("Log with base 10 of array elements : ",np.log10(array_1),"\n")

# calculating the e**x values for x in array 
print(np.exp(array_1),"\n")