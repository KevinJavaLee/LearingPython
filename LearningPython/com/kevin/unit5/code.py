"""
@File    : code.py
@Time    : 2020/7/17 11:31
@Author  : KevinXiao
@Software: PyCharm
"""

# filename = "D:\\python_worksation\\LearningPython\\com\\kevin\\unit5\\myfile\\alice.txt"
#
# try:
#     with open(filename) as word_file:
#         content = word_file.read()
#
# except FileNotFoundError:
#     print("文件没有找到，请重新输出")
# else:
#     word = content.split()
#     length = len(word)
#     print("文件的长度为："+str(length))

# 定义一个函数来解决此问题

def count_words(filename):
    try:
        with open(filename) as word_file:
            content = word_file.read()
    except FileNotFoundError:
        print("文件没有找到了！")
    else:
        word = content.split()
        length = len(word)
        print("文件的长度为"+str(length))

# 调用函数

count_words("myfile\\alice.txt")

# 改进 遍历列表中的文件

file_list = ['myfile\\alice.txt','myfile\\moby_dict.txt','myfile\\little_women.txt']


# 遍历调用
for list in file_list:
    count_words(list)
