"""
@File    : case10-7.py
@Time    : 2020/7/17 15:07
@Author  : KevinXiao
@Software: PyCharm
"""

print("输入两个数字，求和")
print("#"*50)

while True:
    try:
        first_num = int(input("请输入第一个数字："))
        second_num = int(input("请输入第二个数字："))
    except ValueError:
        print("你输入的不是数字！")
    else:
        sum = first_num + second_num
        print("两个数之和为：" + str(sum))