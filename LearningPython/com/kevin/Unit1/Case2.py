"""
@File    : Case2.py
@Time    : 2020/7/4 8:32
@Author  : KevinXiao
@Software: PyCharm
"""
import math
# 循环的使用
# 1.求100以内所有的奇数之和
i = 1
sum = 0
while i < 100 :
    sum += i
    i += 2
print(sum)
print("="*50)

# 2.求100以内所有7的倍数之和，以及个数
j = 1
sum1 = 0

while j < 100 :
    if j % 7 == 0 :
        print(j)
        sum1 += j
        # print("是否进入if判断语句")
    j += 1
print(sum1)

# 3.水仙花数是指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身
# （例如：1**3 + 5**3 + 3**3 = 153）。
#     求1000以内所有的水仙花数

print("="*50)
n = 101
isOK = 0
while n < 1000 :
    single_digit = n % 10
    ten_digit = n // 10 % 10
    hundred_digit = n // 100 # // 表示整除 /带浮点数
    isOK = single_digit ** 3 + ten_digit ** 3 + hundred_digit ** 3
    if isOK == n :
        print(n)
    n += 1

print("="*50)
# 4.获取用户输入的任意数，判断其是否是质数。质数是只能被1和它自身整除的数，1不是质数也不是合数

PrimerNum = int(input("请输入质数：\n"))
index = 2
isFlag = True # 用于标记是否被除1和本身外的其他数整除
while index <= math.sqrt(PrimerNum) :
    if PrimerNum % index == 0 :
        print("这个数不是质数")
        isFlag = False
        break
    #自增
    index += 1
if isFlag :
    print("这是一个质数")

