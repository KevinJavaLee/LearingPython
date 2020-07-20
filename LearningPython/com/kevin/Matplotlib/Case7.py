"""
@File    : Case7.py
@Time    : 2020/7/20 16:30
@Author  : KevinXiao
@Software: PyCharm
"""

from matplotlib import  pyplot as plt

plt.figure(figsize=(20,16),dpi=80)
# 直方图
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]


plt.bar(range(len(interval)),quantity,width=1)

# x的刻度
_x = [i-0.5 for i in range(13)]
interval.append(150)

plt.xticks(_x,interval)
# y轴的刻度设置
plt.yticks(range(min(quantity),max(quantity)+1,100))

# 绘制表格
plt.grid(alpha=0.5)
plt.show()

