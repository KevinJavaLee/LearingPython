"""
@File    : divisionException.py
@Time    : 2020/7/16 20:06
@Author  : KevinXiao
@Software: PyCharm
"""

# try:
#     first_name = input("请输入第一个数字:\n")
#     second_name = input("请输入第二个数字:\n")
#     num = int(first_name) / int(second_name)
# except ZeroDivisionError:
#     print("除数不能为零")
# else:
#
#     print(num)
#

print("请输入两个数字:")
print("输入q退出!")

while True:
    first_num = input("请输入第一个数:")
    if first_num == 'q':
        break
    second_num = input("请输入第二数：")

    if second_num == 'q':
        break
    try:
        sum = int(first_num) / int(second_num)
    except ZeroDivisionError:
        pass
    else:
        print(sum)

