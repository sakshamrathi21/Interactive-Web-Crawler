import matplotlib.pyplot as plt 
import numpy as np 
import random

"""
Title: Monthly Electronics Sales (in thousands)
Data 1: [120, 128, 110, 140, 135, 155, 150, 138, 160, 145, 130, 140]

Title: Monthly Apparel Sales (in thousands)
Data 2: [80, 88, 85, 95, 92, 100, 105, 98, 110, 105, 100, 90]

Title: Monthly Home Goods Sales (in thousands)
Data 3: [40, 45, 50, 52, 48, 55, 50, 45, 40, 35, 30, 35]

Title: Monthly Food and Beverage Sales (in thousands)
Data 4: [200, 210, 195, 220, 230, 220, 215, 205, 200, 190, 180, 190]

Title: Monthly Health and Beauty Sales (in thousands)
Data 5: [90, 100, 95, 110, 105, 115, 120, 118, 125, 122, 110, 105]

Title: Monthly Furniture Sales (in thousands)
Data 6: [70, 75, 80, 72, 85, 90, 82, 78, 75, 70, 68, 72]

extracted from chatgpt 
"""
x_axis=np.linspace(1,12,12)

#plots
electronics_sales = np.array([120, 128, 110, 140, 135, 155, 150, 138, 160, 145, 130, 140])
apparel_sales = np.array([80, 88, 85, 95, 92, 100, 105, 98, 110, 105, 100, 90])
goods_Sales = np.array([40, 45, 50, 52, 48, 55, 50, 45, 40, 35, 30, 35])
food_sales = np.array([200, 210, 195, 220, 230, 220, 215, 205, 200, 190, 180, 190])
beauty_sales = np.array([90, 100, 95, 110, 105, 115, 120, 118, 125, 122, 110, 105])
furniture_sales=np.array([70, 75, 80, 72, 85, 90, 82, 78, 75, 70, 68, 72])

plt.plot(x_axis,electronics_sales,marker='o',label="Monthly Electronics Sales")
plt.plot(x_axis,apparel_sales,marker='o',label="Monthly Apparel Sales")
plt.plot(x_axis,goods_Sales,marker='o',label="Monthly Home Goods Sales")
plt.plot(x_axis,food_sales,marker='o',label=" Monthly Food and Beverage Sales")
plt.plot(x_axis,beauty_sales,marker='o',label="Monthly Health and Beauty Sales")
plt.plot(x_axis,furniture_sales,marker='o',label="Monthly Furniture Sales")

plt.legend(loc="upper left").set_alpha(0.55)

plt.xlabel("Month Number")
plt.ylabel("Sales units(in thousands)")
plt.title("Sales Data")

plt.xticks(range(1,13))
plt.yticks(range(10,400,random.randint(3,5)*10))

plt.show()
