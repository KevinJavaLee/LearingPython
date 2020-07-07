"""
@File    : FactorialTest.py
@Time    : 2020/7/7 11:37
@Author  : KevinXiao
@Software: PyCharm
"""

"""
练习1：求任意数的阶乘

"""
def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n-1)*n

result = fac(3)
print(result)

# 创建一个函数 power 来为任意数字做幂运算 n ** i
# 思想: 10 ** 5 = 10 * 10 ** 4
#

print("#####################")
def power(n,i):
    if i == 1:
        return n
    else:
        return n * power(n,i-1)

power_result = power(10,6)
print(power_result)

print("#"*50)

# 练习
#   创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False
#   回文字符串，字符串从前往后念和从后往前念是一样的

# 方式一：判断是否事回文数
def Palindrome(a):
    length = len(a)
    for i in (0,length//2):
        if a[i] != a[length-1 -i]:
            return False
    return True


print(Palindrome('abba'))
