"""
@File    : Case3.py
@Time    : 2020/7/19 11:07
@Author  : KevinXiao
@Software: PyCharm
"""

# 假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),
# 那么此时如何寻找出气温和随时间(天)变化的某种规律?

from matplotlib import pyplot as plt

# 设置字体的方法 输出中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 数据
a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

# 设置图形的大小
plt.figure(figsize=(20,8),dpi=80)

# 设置x 轴的数据
x_3 = range(1,32)
x_10 = range(51,82)

# 设置散点图
plt.scatter(x_3,a,label="3月份",alpha=0.6)
plt.scatter(x_10,b,label="10月份")


# 设置x轴的刻度
_x_tricks = ["3月{}".format(i) for i in x_3]
_x_tricks += ["10月{}".format(i-50) for i in x_10]
#
_x = list(x_3) + list(x_10)
# 设置刻度
plt.xticks(_x[::3],_x_tricks[::3],rotation=45)
# 设置
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("3、10月份的气温变化图")

#添加图例的位置和样式
plt.legend(loc="upper left")

#
plt.show()