"""
@File    : PiTest.py
@Time    : 2020/7/16 15:30
@Author  : KevinXiao
@Software: PyCharm
"""

# 使用文件中的内容
# 统计文件中放的圆周率的长度

path = "myfile\pi.txt"

# 计算机文件中圆周率的位数
pi_String = ""
with open(path) as pi_file:
    lines = pi_file.readlines()

for line in lines:
    pi_String += line.strip()
len = len(pi_String)
print(len)
#
print(pi_String[:52])


# 测试圆周率是否包含你的生日

with open(path) as name_file:
    lines = name_file.readlines()
# 遍历列表
str = ''
for line in lines:
    str += line.strip()


# 输入生日
birthday = input("请输入你的生日：")
if birthday in str:
    print("你的生日包含在圆周率中")
else:
    print("没有包含在其中")
