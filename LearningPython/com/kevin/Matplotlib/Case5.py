"""
@File    : Case5.py
@Time    : 2020/7/19 18:52
@Author  : KevinXiao
@Software: PyCharm
"""

"""
假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 
2017-09-16(b_16)三天的票房,为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

"""
#
from matplotlib import pyplot as plt

#
plt.rcParams['font.sans-serif'] = ['SimHei']
#
plt.figure(figsize=(20,12),dpi=90)

# 数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

_bar_width = 0.2
_x14 = range(len(a))
_x15= [i+_bar_width for i in _x14]
_x16= [i+_bar_width*2 for i in _x14]

# x轴的数据
plt.bar(_x14,b_14,color="orange",label="14日票房",width=_bar_width)
plt.bar(_x15,b_15,color="red",label="15日票房",width=_bar_width)
plt.bar(_x16,b_16,color="yellow",label="16日票房",width=_bar_width)

# 设置x轴的刻度
plt.xticks(_x14,a)

plt.xlabel("电影名称",loc="right")
plt.ylabel("票房数(单位万元)",loc="top")
plt.title("三日票房变化情况",loc="center")

# 画出图例的样式和位置
plt.legend(loc="upper left")

# 展示图形
plt.show()