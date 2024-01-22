from matplotlib import pyplot as plt
import numpy as np

x_list = [1,2,3,4,5,6,7,8,9,10,11,12]
y1_list = [200,300,400,600,200,700,200,700,400,800,300,400]
y2_list = [200,300,400,600,700,400,800,700,200,200,600,200]


x_indexes = np.arange(len(x_list))
plt.style.use('fivethirtyeight')
plt.bar(x_indexes - 0.2, y1_list, label='Facecream sales data', width=0.4)
plt.bar(x_indexes + 0.2, y2_list, label='Facewash sales data',width=0.4)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

plt.xticks(ticks=x_indexes, labels=x_list)



plt.title('Facewash and Facecream sales data')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('Bar graph.png')
plt.show()

