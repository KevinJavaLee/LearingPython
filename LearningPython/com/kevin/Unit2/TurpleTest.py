"""
@File    : TurpleTest.py
@Time    : 2020/7/5 17:38
@Author  : KevinXiao
@Software: PyCharm
"""

# 元组的使用
# 元组的特点：不可变
# 1.元组的创建
# 方式一：
cars = (1,2,3)
print(cars)
# 方式二：
motos = 'wuyan','qianjiang','jialing'
print(motos)
# 方式三：
trucks = 'volvo','volkswagen','Geely',
print(trucks)

print("#"*50)
# 元组的使用，元组和列表使用一样
# cars[0] = 10 'tuple' object does not support item assignment

# 为a,b,c赋值，如果被赋值的个数少于元组的个数，会报错
a,b,c = cars
print(a)
print(b)
print(c)
print("#"*50)
#
d,*f = motos
print(d)
print(f) # 把其他的当成一个列表赋给后面的数
