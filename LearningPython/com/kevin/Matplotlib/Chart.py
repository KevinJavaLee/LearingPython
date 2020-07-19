"""
@File    : Chart.py
@Time    : 2020/7/18 9:45
@Author  : KevinXiao
@Software: PyCharm
"""

# 导入matplotlib 库
from matplotlib import pyplot as plt

# figure 通过实例一个figure并且传递参数，能够在后台自动自动使用figure的实例
plt.figure(figsize=(200,100),dpi=80)

# 指定x轴的数据
x = range(2,26,2)
# 指定y轴的数据
y = [12,33,9,30,67,34,54,15,30,43,12,4]

# 设置x轴的刻度
# plt.xticks(x)
# 设置y轴的刻度




plt.plot(x,y)

# 保存图片到本地
# plt.savefig("plot.png")
plt.show()


