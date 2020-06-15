# k@mlesh
# h3avren
"""
Matplotlib is a famous python library used to plot 2d and 3d graphs.
installation :

"""
import matplotlib.pyplot as plt
import numpy as np

age = [25,26,27,28,29,30,31,32,33,34,35]    # age data to be plotted
median_salary_for_all = [38496,42000,46752,49320,53200,56000,62366,64928,67317,68748,73752]    # salary data to be plotted
median_salary_for_government_employees = [33496,32000,42552,50320,51240,53100,68536,68928,69317,70748,77552]
median_salary_for_private_employees = [32176,48700,41852,41430,55460,56999,61176,61588,61187,61968,71592]

barWidth = 0.25
x_axis = np.arange(len(age))
plt.bar(x_axis-barWidth,median_salary_for_all,width=barWidth,color="Blue",label="All Emp.")
plt.bar(x_axis,median_salary_for_government_employees,width=barWidth,color="Yellow",label="Gov. Emp.")
plt.bar(x_axis + barWidth,median_salary_for_private_employees,width=barWidth,color="Black",label = "Private Emp.")

plt.title("Median Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.xticks(ticks=x_axis,label=age)
plt.legend()
plt.show()