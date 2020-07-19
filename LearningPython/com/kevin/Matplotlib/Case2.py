"""
@File    : Case2.py
@Time    : 2020/7/18 19:34
@Author  : KevinXiao
@Software: PyCharm
"""

from matplotlib import pyplot as plt
# 练习2
# 设置字体的方法 输出中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(100,80),dpi=80)

a = [1,0,1,1,1,4,3,2,3,4,4,5,6,5,4,3,1,1,1]
b = [1,0,0,1,1,4,3,2,3,4,2,4,5,6,5,3,1,1,3]
x = range(11,30)

# 设置折线的线条颜色 alpha 表示透明度  linestyle表示线条的风格 linewidth设置线条的风格
plt.plot(x,a,label="同学",linewidth=3,linestyle="--",alpha=0.5)
plt.plot(x,b,label="自己")
xticks_label = ["{}岁".format(i) for i in x]

# 调整x轴的刻度和样式
plt.xticks(x,xticks_label)

# 设置网格
plt.grid(alpha=0.4)

# 添加图例
plt.legend(loc="upper left")

plt.show()

