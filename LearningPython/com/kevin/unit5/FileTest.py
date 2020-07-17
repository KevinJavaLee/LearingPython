"""
@File    : FileTest.py
@Time    : 2020/7/16 15:07
@Author  : KevinXiao
@Software: PyCharm
"""


with open("myfile/hello.txt") as helloFile:
    text = helloFile.read()
    print(text)

# 逐行读取

pathName = "myfile/word.txt"

with open(pathName) as file_object:
    for text in file_object:
        print(text.strip())
# 创建一个包含文件各行的内容的列表
with open(pathName) as file_object:
    # 读取文件中每一行内容，作为列表中的元素
    lines = file_object.readlines()
print(lines)


