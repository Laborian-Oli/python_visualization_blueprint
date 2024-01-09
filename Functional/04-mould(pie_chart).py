"""
 Author: 2020200229
 Creation time: 2023/4/2
 Filename: 04-mould(pie_chart)
 """
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('default')  # 套用Style
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(8, 6))  # 画布大小

x = np.array(["甲", "乙", "丙", "丁"])
y = np.array([85, 64, 44, 18])
interval = np.array([0.2, 0, 0, 0])
# color_array = np.array([100, 80, 60, 40])
colors = plt.cm.summer(np.arange(len(x))/len(x))  # 这行是干什么的来着？为什么cm.summer()不存在还可以正常画图？


# plt.get_cmap('summer')

plt.pie(y, explode=interval, labels=x, colors=colors, autopct='%.2f%%', pctdistance=0.6, shadow=False,
        labeldistance=1.1, startangle=0, radius=0.8, counterclock=True, wedgeprops=None, textprops=None,
        center=(0, 0), frame=False, rotatelabels=False)

# 显示图例
plt.legend(loc='best')

plt.title('各项占比', loc='center')

plt.show()
