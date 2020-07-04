"""
@File    : LoopCase.py
@Time    : 2020/7/4 8:51
@Author  : KevinXiao
@Software: PyCharm
"""
import  math
# 练习1：
#     打印99乘法表
#     1*1=1
#     1*2=2 2*2=4
#     1*3=3 2*3=6 3*3=9
#     ...                 9*9=81
row = 1 # 控制外层循环
col = 1 # 控制内层循环

while row <= 9:
    col = 1 # 每打印一行之后 col 重新赋值为1
    while col <= row :
        print(f'{col}*{row}={col*row}',end=' ')
        col += 1
    print()
    row += 1 # 没输出一行内容加一

print("="*50)

# 求100以内所有的质数
num = 2 #从2开始判断该数是否是质数
while num < 100 :
    index = 2 # 作除数
    isFlag = True
    while index <= math.sqrt(num) :
        if num % index == 0 :
            isFlag = False
            break
        #
        index += 1

    if isFlag :
        print(num)
    num += 1
