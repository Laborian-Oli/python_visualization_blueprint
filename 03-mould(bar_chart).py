"""
 Author: 2020200229
 Creation time: 2023/4/2
 Filename: 03-mould(bar_chart)
 """
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('default')  # 套用Style
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(8, 6))  # 画布大小

x = np.array(["甲", "乙", "丙", "丁"])
y = np.array([85, 64, 44, 18])
colors = plt.cm.summer(np.arange(len(x))/len(x))

plt.cm.get_cmap('summer')
plt.bar(x, y, color=colors)
# plt.barh(x, y)  # 条形图

# plt.axis([-5, 5, -2, 25])  # 坐标轴尺度，一般不需要
# plt.tick_params(axis='both', which='major', labelsize=10)  # 坐标轴刻度

plt.grid(visible=True, which='major', axis='both', linestyle='-.')  # 网格线

plt.title('考生分数', loc='center')
plt.xlabel('考生', loc='right')  # 使用条形图时需要修改
plt.ylabel('分数', loc='top')

plt.show()
