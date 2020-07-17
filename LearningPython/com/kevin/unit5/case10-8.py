"""
@File    : case10-8.py
@Time    : 2020/7/17 16:36
@Author  : KevinXiao
@Software: PyCharm
"""


filename = "myfile\\dog.txt"
dogfile = "myfile\\cat.txt"
try:
    with open(filename) as cat_file:
        cats = cat_file.readlines()
        with open(dogfile,"a") as dog_file:
            for cat in cats:
                dog_file.write(cat)
except FileNotFoundError:
    print("文件没有找到")
else:
    print("写入完毕")
