"""
@File    : ListDeom.py
@Time    : 2020/7/3 16:59
@Author  : KevinXiao
@Software: PyCharm
"""

# 列表
str = [12,33,44,55]
print(type(str))
print(str)

# 元组
str1 = (344,555,666)
print(type(str1))
print(str1)

# 集合
str2 = {1.23,3,5,66}
print(type(str2))
print(str2)

# 相互之间的转换
# list --> tuple
print(tuple(str))
print(str) # 转换之后 本身并没有发生改变

# tuple --> list
print(list(str1))
print(str1)

# list --> set
print(set(str))
print(set(str1))