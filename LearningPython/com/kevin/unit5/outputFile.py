"""
@File    : outputFile.py
@Time    : 2020/7/16 16:21
@Author  : KevinXiao
@Software: PyCharm
"""


# 写入文件

path = "myfile\output.txt"
with open(path,"w") as obj_file:
    obj_file.write("kuangzong niubi")
    obj_file.write("\nniubility")
# 像文本文件中追加内容
with open(path,"a") as obj_file:
    obj_file.write("kuangzong niubi")
    obj_file.write("\nniubility")
