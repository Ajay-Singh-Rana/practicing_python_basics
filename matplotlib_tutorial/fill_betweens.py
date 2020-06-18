from matplotlib import pyplot as plt

year = [2000,2002,2004,2006,2008,2010,2012,2014,2016,2018]
apple_prices = [80,60,70,55,85,75,90,65,80,75]
mango_prices = [80,90,85,95,75,80,60,60,90,85]

plt.plot(year,apple_prices,color="#2333ef",label = "Apple")
plt.plot(year,mango_prices,color="#ec3421",label = "Mango")

plt.title("Fill Betweens")
plt.xlabel("Year")
plt.ylabel("Prices")

plt.fill_between(year,mango_prices,apple_prices,where=(apple_prices > mango_prices),color="#ff2121",alpha=0.2,interpolate=True)
plt.fill_between(year,mango_prices,apple_prices,where=(apple_prices <= mango_prices),color="#12ff21",alpha=0.2,interpolate=True)
plt.legend()
plt.tight_layout()
plt.show()