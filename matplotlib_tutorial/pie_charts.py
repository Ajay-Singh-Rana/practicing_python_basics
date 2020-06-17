from matplotlib import pyplot as plt

plt.xkcd()  # uses the skcd style for the pie chart plot

most_selling_fruits = [35.5,23,8,25.5,8,20] # the data to be plotted
fruits = ["Banana","Mango","Grape","Apple","Oranges","Watermelon"]  # labels for the data
section_color = ["#ba28dc","#ab34ff","#334455","#00bbaa","#2abc10","#030405"]   # colors for corresponding fruit
explode_values = [0.1,0.1,0.1,0.1,0.1,0.1]    # explode values

plt.pie(most_selling_fruits,colors=section_color,labels=fruits,wedgeprops={"edgecolor":"black"},explode=explode_values,shadow=True,autopct="%1.1f%%")
# autopct is used to display the percentage of each category
# explode is an attribute that defines by how much of the radius size would the pie_sections be cut off
# shadow if set to 'True' gives a 3d looking pie chart with a shadow. 
plt.tight_layout()
plt.show()