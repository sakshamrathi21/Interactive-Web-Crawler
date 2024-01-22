from matplotlib import pyplot as plt

x_list = [1,2,3,4,5,6,7,8,9,10,11,12]
y_tp1 = [120, 130, 110, 140, 125, 135, 115, 145, 130, 120, 110, 150]
y_tp2 = [110, 125, 135, 120, 130, 115, 140, 125, 130, 110, 150, 120]
y_tp3 = [130, 120, 140, 115, 125, 135, 110, 150, 120, 130, 110, 140]
y_tp4 = [140, 110, 130, 125, 135, 120, 115, 145, 130, 120, 140, 110]


y_fc = [90, 100, 95, 105, 92, 98, 85, 110, 100, 92, 88, 105]
y_fw = [80, 85, 92, 88, 90, 95, 100, 82, 105, 88, 98, 90]

plt.style.use('fivethirtyeight')
plt.plot(x_list, y_fc, marker = '.', linewidth=2, label='Face cream sales data')
plt.plot(x_list, y_fw, marker = '.', linewidth=2, label='Face wash sales data')
plt.plot(x_list, y_tp1, marker = '.', linewidth=2, label='ToothPaste sales data')
plt.plot(x_list, y_tp2, marker = '.', linewidth=2, label='ToothPaste sales data')
plt.plot(x_list, y_tp3, marker = '.', linewidth=2, label='ToothPaste sales data')
plt.plot(x_list, y_tp4, marker = '.', linewidth=2, label='ToothPaste sales data')



#plt.hlines['top'].set_visible(True)
# plt.spines['right'].set_visible(True)
# plt.spines['bottom'].set_visible(True)
# plt.spines['left'].set_visible(True)

plt.axvline(0, color='k', linewidth = 0.8)
plt.axhline(0, color='k', linewidth = 0.8)

plt.legend()
plt.title('Sales Dta')
plt.ylabel('Sales unit in number')
plt.xlabel('Month Number')
plt.tight_layout()
plt.grid(False)
plt.savefig('Line chart.png')
plt.show()
