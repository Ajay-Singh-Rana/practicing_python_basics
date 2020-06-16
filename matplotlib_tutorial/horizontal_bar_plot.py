from matplotlib import pyplot as plt

plt.style.use("ggplot")

variations_in_price_of_apple = [55,70,90,65,70,50,80,85,95,55,60,75,80,90,60]
year = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]

plt.barh(year,variations_in_price_of_apple,color="#1122ee",label="Price")   # method to plot horizontal bar graphs
plt.xlabel("Price")
plt.ylabel("Year")
plt.title("variations in price of apple")

plt.xticks(ticks=variations_in_price_of_apple,label=variations_in_price_of_apple)
plt.legend()

# mixing line plot with bar plot
plt.plot(variations_in_price_of_apple,year)

plt.tight_layout()
plt.show()