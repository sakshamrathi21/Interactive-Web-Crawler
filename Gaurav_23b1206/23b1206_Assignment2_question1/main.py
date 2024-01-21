import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y1 = [9000,6000,9000,5555,2948,4654,9255,8765,3456,7654,9878,2345]
y2 = [5478,8931,3210,6654,4567,9876,2345,7890,1102,8765,4321,5896]
y3 = [4523, 7890, 2345, 6789, 5432, 9876, 1204, 6543, 1101, 8899, 3521, 9856]
y4 = [5678, 8765, 4321, 9999, 2345, 7890, 6543, 1200, 5432, 8899, 1104, 7892]
y5 = [3456, 7890, 5432, 1204, 9876, 6543, 1101, 8899, 2345, 6789, 3521, 9856]
y6 = [6789, 5432, 7890, 2345, 1104, 7892, 6543, 1200, 5436, 9854, 3521, 8899]
plt.plot (x,y1,label = "Face cream sales data", linewidth=5)
plt.plot (x,y2, label = "Face cream sales data", linewidth=5)
plt.plot (x,y3, label = "Face cream sales data", linewidth=5)
plt.plot (x,y4, label = "Face cream sales data", linewidth=5)
plt.plot (x,y5, label = "Face cream sales data", linewidth=5)
plt.plot (x,y6, label = "Face cream sales data", linewidth=5)
plt.scatter (x,y1,s=100)
plt.scatter (x,y2,s=100)
plt.scatter (x,y3,s=100)
plt.scatter (x,y4,s=100)
plt.scatter (x,y5,s=100)
plt.scatter (x,y6,s=100)
plt.legend(loc = 'upper left')
plt.title("Sales Data")
plt.ylabel("Sales Unit In Number")
plt.xlabel("month number")
plt.show()