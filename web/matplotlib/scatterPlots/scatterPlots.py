# h3avren
# k@mlesh

# Scatter Plots

# Scatter Plot has points that shows relationship between two sets of data.
# In order to draw a scatter plot with matplotlib we use the scatter() method.

# imports
from matplotlib import pyplot as plt
import numpy as np


# using a built-in matplotlib style for the plot
plt.style.use("seaborn")

"""
To use a style we need to call the use method of the style object for the pyplot (plt) and pass it the name of the style that you wish to use. We have the following styles to choose from
"""

# Writing down the data

# price and ratings for few products
price = np.array([1000,2343,3334,4535,555,6344,734,85,966,1033])
ratings = np.array([6,7,7,7,3,8,3,2,4,6])

# plotting
plt.scatter(price,ratings)

plt.title('Product Ratings vs Price')

plt.xlabel('Price')
plt.ylabel('Ratings')

plt.show()

# Setting the size for the markers on the plot

"""to set the size for the markers we need to pass a size value to the "s" argument and the size for these markers should be in double or triple digits otherwise the resulting markers are going to be too tiny cause the s argument expects size value to be of the form point**2."""

plt.scatter(price,ratings,s=60)

plt.title('Product Ratings vs Price')

plt.xlabel('Price')
plt.ylabel('Ratings')

plt.show()

# changing the marker shape,color and setting its linewidth

"""
The marker can be changed by passing the desired marker style to the 'marker' attribute and the color can be changed using the 'c' argument as for the linewidth we need to pass the desired vlaue for the width of the line to the 'linewidths' argument.Passing a color value to the edgecolor gives our marker a color on the edges.
"""

plt.scatter(price,ratings,s=150,c="green",marker="X",edgecolor="black",linewidths=1,alpha=0.85)    
# alpha just decides the intensity of the color,the color is more intense towards 1 than towards 0

plt.title('Product Ratings vs Price')

plt.xlabel('Price')
plt.ylabel('Ratings')

plt.show()

# Adding a color bar to the scatter plot

"""
we use a colorbar to get more visually good looking and informative plots, these are a colorscale where the varying color of the markers are indicated as a comparision scale so obviously we need to provide different color values to each point
"""

# defining colors array for every point
colors = np.array([4,5,8,9,3,7,0,3,5,10])    # this array is then passed on to the c attribute

plt.scatter(price,ratings,s=150,c=colors,cmap="Greens",marker="X",edgecolor="black",linewidths=1)

colorbar = plt.colorbar()
colorbar.set_label('Ratings Vs Price')

plt.title('Product Ratings vs Price')

plt.xlabel('Price')
plt.ylabel('Ratings')

plt.show()

# plotting a scatter plot on a logarithmic scale

plt.scatter(price,ratings,s=150,c=colors,cmap="Greens",marker="X",edgecolor="black",linewidths=1)#,alpha=0.85)

# to plot a scatter plot on a logarithmic scale we have to set the scale for the abscissa's  to 'log'
plt.xscale('log')   # setting the xscale to 'log'
plt.yscale('log')   # setting the ysclae to 'log'

colorbar = plt.colorbar()
colorbar.set_label('Ratings Vs Price')

plt.title('Product Ratings vs Price')

plt.xlabel('Price')
plt.ylabel('Ratings')

plt.show()


# That's it for today...See you in the next tutorial...Until then a H3avren style Ta-Da...