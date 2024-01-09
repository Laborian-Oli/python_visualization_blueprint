"""
 Author: 2020200229
 Creation time: 2023/3/24
 Filename: 01-mould
 """
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('default')  # 套用Style
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(6, 6))  # 画布大小

x = list(np.linspace(-2, 2, num=21))  # num参数为数列个数，设置为奇数，使得间隔为偶数个
y_sin = [np.sin(i) for i in x]
y_cos = [np.cos(i) for i in x]
y_tan = [np.tan(i) for i in x]
y_exp = [i**2 for i in x]

plt.plot(x, y_sin, label='SIN', linewidth=1, linestyle='-', marker='+', markersize=5)
plt.plot(x, y_cos, label='COS', linewidth=1, linestyle='--', marker='.', markersize=5)
plt.plot(x, y_exp, label='抛物线', linewidth=1, linestyle=':', marker='*', markersize=5)
plt.legend(loc='best')

# plt.axis([-5, 5, -2, 25])  # 坐标轴尺度，一般不需要
# plt.tick_params(axis='both', which='major', labelsize=10)  # 坐标轴刻度

plt.grid(visible=True, which='major', axis='both', linestyle='-.')  # 网格线

plt.title('基本初等函数的函数图像', loc='center')
plt.xlabel('X轴', loc='right')
plt.ylabel('Y轴', loc='top')

plt.show()
