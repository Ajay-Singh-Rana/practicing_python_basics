# k@mlesh
# h3avren
from matplotlib import pyplot as plt

rounds = [1,2,3,4,5,6,7,8,9,10]
player_1 = [3,2,1,6,4,3,5,8,1,9]
player_2 = [1,2,4,3,2,1,3,1,3,3]
player_3 = [1,1,1,2,2,2,4,5,6,3]

labels_list = ["player_1","player_2","player_3"]
colors_list = ["#fe9821","#3238ee","#34ef89"]
plt.stackplot(rounds,player_1,player_2,player_3,labels=labels_list,colors=colors_list)  # stakplot() method is used to draw stackplots
plt.title("Stackplot")
plt.xlabel("time")
plt.ylabel("points")
plt.legend(loc="upper left")    # sets the location of the legend as the upper left
plt.tight_layout()
plt.show()