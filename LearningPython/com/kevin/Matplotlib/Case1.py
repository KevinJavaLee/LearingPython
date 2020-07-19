"""
@File    : Case1.py
@Time    : 2020/7/18 19:08
@Author  : KevinXiao
@Software: PyCharm
"""

from matplotlib import pyplot as plt
import random

# 练习1

# 设置字体的方法 输出中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(60,80),dpi=80)
# 两个小时的气温变化

x = range(0,120)

# y轴的温度变化

y = [random.randint(20,35) for i in range(120)]
plt.plot(x,y)
# 调整x轴的刻度
_xticks_label = ["10点{}".format(i) for i in range(60)]
_xticks_label += ["11点{}".format(i) for i in range(60)]

# 设置
plt.xticks(list(x)[::3],_xticks_label[::3],rotation=45)

plt.title("10点到12点的气温变化图")
plt.xlabel("时间")
plt.ylabel("温度 单位()")

plt.show()


