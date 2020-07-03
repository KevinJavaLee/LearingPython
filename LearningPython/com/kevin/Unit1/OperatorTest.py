"""
@File    : OperatorTest.py
@Time    : 2020/7/3 19:56
@Author  : KevinXiao
@Software: PyCharm
"""

# 与java 不同点
# 逻辑运算符 and or
# 算术运算符 比较运算符 一样
# python 没有自增自加运算符

# and
num = 0 and 1
num1 = 1 and 2
num2 = 2 and 1
print(num)
print(num1)
print(num2)
# 结论：遇到0则结果为零 否则值为后一个数的值
print("---------------------")
# or 或运算

cnt = 0 or 0
cnt1 = 0 or 1;
cnt2 = 1 or 2;

print(cnt)
print(cnt1)
print(cnt2)
# 结论 都为零才为零 否则为第一个不为零的数
