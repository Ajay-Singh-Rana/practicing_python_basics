# k@mlesh
# h3avren
from matplotlib import pyplot as plt   # importing the plotting library

# plt.xkcd()  # to use xkcd comic style plotting
plt.style.use("fivethirtyeight")
age = [25,26,27,28,29,30,31,32,33,34,35]    # age data to be plotted
median_salary_for_all = [38496,42000,46752,49320,53200,56000,62366,64928,67317,68748,73752]    # salary data to be plotted
median_salary_for_government_employees = [33496,32000,42552,50320,51240,53100,68536,68928,69317,70748,77552]
median_salary_for_private_employees = [32176,48700,41852,41430,55460,56999,61176,61588,61187,61968,71592]
plt.title('Median Salary (USD) by age')    # providing the plot a title

# plotting line for median salary of all types of employees collectively
plt.plot(age,median_salary_for_all,marker="v",linestyle="-.",color="Blue",linewidth=2,label="All Emp.")  # plotting the data,providing the formatting string and label to the plotted line

# plotting line for median salary for government employees
plt.plot(age,median_salary_for_government_employees,marker="o",linestyle="-",color = "Green",linewidth=2,label="Gov. Emp.")

# plotting line for median salary for private firm employees
plt.plot(age,median_salary_for_private_employees,marker="H",linestyle=":",color="Black",linewidth=2,label="Private Emp.")

plt.xlabel("Age")   # providing the x-axis a label
plt.ylabel("Salary")    # providing the y-axis a label
plt.tight_layout()  # a function that automatically adjusts the plot parameters to provide the right padding
plt.legend()    # so that the plot uses the labels to provide the line their respective legends
plt.grid(True)  # to draw a grid over the plot
plt.savefig("line_plotting.png")    # to save the plot locally as a png image
plt.show()  # to display the plot