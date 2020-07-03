"""
@File    : Case1.py
@Time    : 2020/7/3 20:39
@Author  : KevinXiao
@Software: PyCharm
"""
# 三目运算符
# 表达式1 if 判断语句 else 表达式2
#   判断语句true 执行表达式1 否则表达式1
#   判断语句false 执行表达式2 否则表达式2

a = 30
b = 20
c = 40
# 求两个数的最大值
print(a) if a > b  else print(b)
print("---------------")
# 求三个数的最大值
# 方法一：
max = a if a > b else b
max = max if max > c else c
print(max)
print("________________")
# 方法二：
maxNum = a if a > b and a > c else b if b > c else c
print(maxNum)
# 运算符的优先级
# 算术运算符(and > or   )>关系运算符>逻辑运算符
