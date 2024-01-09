"""
 Author: 2020200229
 Creation time: 2023/3/30
 Filename: 02-mould(scatter_plot)
 """
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('default')  # 套用Style
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(8, 6))  # 画布大小

step = 21
x = list(np.linspace(-2, 2, num=step))  # num参数为数列个数，设置为奇数，使得间隔为偶数个
y_sin = np.array([np.sin(i) for i in x])
y_cos = np.array([np.cos(i) for i in x])
y_tan = np.array([np.tan(i) for i in x])
y_square = np.array([i**2 for i in x])

# 散点大小，按照实际数据大小调整
sin_area = (25 * np.random.rand(step)) ** 2 / 2
cos_area = (25 * np.random.rand(step)) ** 2 / 2
square_area = (25 * np.random.rand(step)) ** 2 / 2

# 这里只用符号区别数据，用颜色区别大小
plt.scatter(x, y_sin, c=np.random.randint(0, 100, step), label='SIN',
            marker='o', s=sin_area, alpha=0.8, cmap='Reds')
plt.colorbar()
plt.scatter(x, y_cos, c=np.random.randint(0, 100, step), label='COS',
            marker='v', s=cos_area, alpha=0.8, cmap='Blues')
plt.colorbar()
plt.scatter(x, y_square, c=np.random.randint(0, 100, step), label='抛物线',
            marker='*', s=square_area, alpha=0.8, cmap='Greens')
plt.colorbar()

# 显示图例
plt.legend(loc='best')

# plt.axis([-5, 5, -2, 25])  # 坐标轴尺度，一般不需要
# plt.tick_params(axis='both', which='major', labelsize=10)  # 坐标轴刻度

plt.grid(visible=True, which='major', axis='both', linestyle='-.')  # 网格线

plt.title('基本初等函数的函数图像', loc='center')
plt.xlabel('X轴', loc='right')
plt.ylabel('Y轴', loc='top')

plt.show()
