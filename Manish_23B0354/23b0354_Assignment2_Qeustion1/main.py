import matplotlib.pyplot as plt
import numpy as np 
import random

x_axis_1=np.linspace(1,12,12)-0.1
y_axis_1=np.random.random(12)*4000
plt.bar(x_axis_1,y_axis_1,width=0.2,label="Face Cream sales data")

x_axis_2=np.linspace(1,12,12)+0.1
y_axis_2=np.random.random(12)*4000
plt.bar(x_axis_2,y_axis_2,width=0.2,label="Face Wash sales data")

plt.grid(ls='--')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title("Facewash and facecream sales data")

plt.xticks(range(1,13))
plt.yticks(range(500,4000,500))

plt.legend(loc="upper left").set_alpha(0.6)
plt.show()
