"""
@File    : FileNotFound.py
@Time    : 2020/7/17 11:22
@Author  : KevinXiao
@Software: PyCharm
"""
try:
    filename = 'alice.txt'
    #
    with open(filename) as obj_file:
        text = obj_file.readline()
except FileNotFoundError:
    print("文件没有找到")
else:
    print(text)