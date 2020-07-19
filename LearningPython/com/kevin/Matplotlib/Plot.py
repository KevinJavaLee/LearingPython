"""
@File    : Plot.py
@Time    : 2020/7/18 15:35
@Author  : KevinXiao
@Software: PyCharm
"""
# # 导入matplotlib 库
# from matplotlib import pyplot as plt
#
# # figure 通过实例一个figure并且传递参数，能够在后台自动自动使用figure的实例
# plt.figure(figsize=(200,100),dpi=80)
#
# # 指定x轴的数据
# x = range(2,26,2)
# # 指定y轴的数据
# y = [12,33,9,30,67,34,54,15,30,43,12,4]
#
# # 设置x轴的刻度
# # plt.xticks(x)
# # 设置y轴的刻度
#
# plt.plot(x,y)
# plt.show()

from matplotlib import pyplot as plt

plt.figure(figsize=(100,80),dpi=80)

# x轴上的数据是可迭代的
x = range(2,26,2)
# y轴坐标上对应的数据
y = [15,13,14,17,20,25,26,26,24,22,18,15]

plt.plot(x,y)

# 设置x轴的刻度
# plt.xticks(x)
# 求2-到25
_xticks_label = [i/2 for i in range(2,50)]

# 从第16个数开始 步长为3
plt.xticks(_xticks_label[15::3])
# 设置y轴的刻度
plt.yticks(range(min(y),max(y)))

plt.show()