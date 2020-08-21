# h3avren
# k@mlesh

# Histograms
# A histogram is an approximate representation of the distribution of numerical data.To construct a histogram,the first step is to <b>bin</b> the range of values (dividing the entire range of values into a series of intervals) the data.Follow the following steps to plot histograms with the help of matplotlib and Python.

# imports
from matplotlib import pyplot as plt
import numpy as np


# organizing the data

# different ages among bookreaders in a library
ages = np.array([14,15,17,19,21,23,24,27,29,33,35,36,37,39,41,43,45,49,50])

# bins
# bins are used to group the data
bins = np.array([10,20,30,40,50,60])


# plotting 
plt.hist(ages,bins)

"""
The hist() method is used to plot a histogram, the first parameter is the set of values to be plotted and the second yet not mandatory attribute is bins which is used to group the data to be plotted
"""

plt.title("Age Distribution Among Bookreaders")

plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# adding an edge color to the plot
# adding an edge color is as simple as passing the edgecolor with a color value
plt.hist(ages,bins,edgecolor="black")

plt.title("Age Distribution Among Bookreaders")

plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# changing colors for the bars

# color
color =  ["#ddaa11"]

# we can change the default color of our bars by passing the color value to the color argument
plt.hist(ages,bins,color=color,edgecolor="Black")

plt.title("Age Distribution Among Bookreaders")

plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# plotting a chart on a logarithmic scale
"""When a large dataset isn given then a few groups within the data might become obscure in comparison with another group,that's the reason a plot with a logarithmic scale is plotted."""

# data 
population = np.array([10,20,30,33,34,35,36,37,38.5,39,50,39.5])

age_groups = np.array([30,32,34,36,38,40,42])

# plotting 
plt.hist(population,age_groups,color=color,edgecolor="Black",log=True)

plt.title("Age Distribution Among Bookreaders")

plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# That's it for today...See you in the next tutorial...Until then a H3avren style Ta-Da...

