# h3avren
# k@mlesh

# Stack Plots

"""
A Stack Plot is a plot that shows the whole data set with easy visualization of how each part makes up the whole. 
Each constituent of the stack plot is stacked on top of each other. It shows the part makeup of the unit,as well as the whole unit.
"""
# Importing the libraries

from matplotlib import pyplot as plt
import numpy as np

# Getting the data ready

# cricket matches 
matches = np.array([1,2,3,4,5,6])

# scores by top 3 players of a both sides
player_1 = np.array([100,45,80,85,95,56])
player_2 = np.array([10,45,56,36,89,114])
player_3 = np.array([100,20,10,5,18,111])

# Plotting the data to a stackplot

plt.stackplot(matches,player_1,player_2,player_3)   # the stackplot() method is used to plot a stackplot

plt.title("Scores By Top 3 Players")
plt.tight_layout()
plt.show()

# Providing labels

labels = np.array(["Player_1","Player_2","Player_3"])

plt.stackplot(matches,player_1,player_2,player_3,labels=labels) # the labels argument is responsible to give labels to the plot

plt.title("Scores By Top 3 Players")
plt.tight_layout()
plt.legend() # the legend() method adds the labels to the legend and displays it
plt.show()

# Changing the location of the legend and adding colors of choice

# colors
colors = np.array(["#33fff0","#ff771d","#302df1"])  # the colors array

plt.stackplot(matches,player_1,player_2,player_3,labels=labels,colors=colors)   
# passing the colors argument a set of colors sets the colors for the plot

plt.title("Scores By Top 3 Players")
plt.tight_layout()
plt.legend(loc="upper left")    # passing the loc either a tuple or a string sets the location of the legend
# "upper left" places the legend on the upper left corner of the plot

plt.show()

# Extras ;););)
"""
 We can plot a stack plot by passing a single multidimension array instead of passing arrays seperately. 
It's like each dimension of the array will be treated as an individual array argument. 
"""

# redefining the data as a multi-dimensional array
players= np.array([[100,45,80,85,95,56],[10,45,56,36,89,114],[100,20,10,5,18,111]])

# plotting
plt.stackplot(matches,players,labels=labels,colors=colors)   
# passing the multi-dimensional array

plt.title("Scores By Top 3 Players")
plt.tight_layout()
plt.legend(loc="upper left") 
plt.show()

# That's it for today...See you in the next tutorial...until then, a <em>H3avren</em> style Ta-Da...