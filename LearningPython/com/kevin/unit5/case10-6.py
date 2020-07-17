"""
@File    : case10-6.py
@Time    : 2020/7/17 15:02
@Author  : KevinXiao
@Software: PyCharm
"""

try:
    first_num = int(input("请输入第一个数字："))
    second_num = int(input("请输入第二个数字："))
except ValueError:
    print("你输入的不是数字！")
else:
    sum = first_num + second_num
    print("两个数之和为："+str(sum))

