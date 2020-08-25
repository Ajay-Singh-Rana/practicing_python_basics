# h3avren
# k@mlesh

# Plotting Date Based Data

# To plot the date based data we have plot_date() method in matplotlib.

# imports
from matplotlib import pyplot as plt
from datetime import datetime   # so as to store dates in the correct format instead of storing these as a string
import numpy as np

# collecting date based data
date = np.array([datetime(2020,3,2),datetime(2020,3,3),datetime(2020,3,4),datetime(2020,3,5),datetime(2020,3,7),datetime(2020,3,6),datetime(2020,3,8)])
price = np.array([11.2,11.3,11.4,11.5,11.6,11.4,11])


# plotting
plt.plot_date(date,price,linestyle="-") # if we do not use a linestyle we get scattered points by default

plt.gcf().autofmt_xdate()   # that's how we tilt the xtciks of the date for the sake of clarity

# gcf() is the method to get the current figure,we can manipulate the plot figure using this function

plt.title("Price Variations")

plt.xlabel("Dates")
plt.ylabel("Price")

plt.tight_layout()

plt.show()

# sorting and formatting dates

# though the previous plot seems to be perfect but it has a glitch in it
# as the date 6-8-2020 comes later in the array so the graph is wrongly plotted at that point 
# and what if we want to change our date fomrat to date-month_nam-year ? we can achieve that by passing a format string to the 
# DateFormatter class of matplotlib dates

# importing matplotlib dates
from matplotlib import dates as mpl_dates

# sorting our dates array using the numpy sort function
date = np.sort(date)

# plotting the graph with the sorted data 
plt.plot_date(date,price,linestyle="-")

plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter("%d,%b %Y")  # that's a format string there are more such format strings that can be checked in the documentation

plt.gca().xaxis.set_major_formatter(date_format) # function to change the dates on the x-axis

plt.title("Price Variations")

plt.xlabel("Dates")
plt.ylabel("Price")

plt.tight_layout()

plt.show()

# Note: 
# While reading data from a csv file we might require to change the date data into datetime format as csv file holds data as string.So it would be convenient to use <b>pandas</b> for reading a csv file as it provides fucntionality to parse string data into a datetime format. 


# That's it for today...see you in the next tutorial...until then a H3avren style Ta-Da...