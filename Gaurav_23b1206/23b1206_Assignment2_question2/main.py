import matplotlib.pyplot as plt 
x = [1,2,3,4,5,6,7,8,9,10,11,12]
x1 =[]
x2 = []
for a in x:
    x1.append(a - 0.125)
for a in x:
    x2.append(a + 0.125)
y1 = [2431, 1789, 2150, 2896, 1325, 2654, 2011, 1123, 1567, 2934, 1245, 2778]
y2 = [2212, 1988, 2789, 1566, 2977, 1023, 2345, 2750, 1299, 1867, 2634, 1422]
plt.bar(x1 ,y1,color = "blue",width=0.25,label = "face cream sales data")
plt.bar(x2 ,y2,color = "orange",width=0.25,label = "facewash sales data")
plt.title("facewash and face cream sales data")
plt.ylabel("sales units in number")
plt.xlabel("month number")
plt.legend(loc = 'upper left')
plt.show()
