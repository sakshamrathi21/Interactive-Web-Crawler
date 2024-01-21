import matplotlib.pyplot as plt 
import numpy as np 
x1= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x2= np.array([1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3,11.3,12.3])
y1= np.array([2500,2600,2200,3400,3700,2700,3000,3800,3600,2000,2300,2900])
y2= np.array([1500,1200,1300,1100,1700,1600,1100,1400,1700,1800,2100,1650]) 
plt.grid(linestyle='dashed')
plt.xlabel('Month Number')
plt.ylabel("sales units in number")
plt.title('facewash and facecream sales data')
plt.bar(x1,y1,color="blue",width=0.3,label="face cream sales data")
plt.bar(x2,y2,color="red",width=0.3,label="face wash sales data")
plt.legend()
plt.show()