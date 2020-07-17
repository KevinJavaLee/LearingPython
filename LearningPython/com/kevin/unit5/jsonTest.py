"""
@File    : jsonTest.py
@Time    : 2020/7/17 16:50
@Author  : KevinXiao
@Software: PyCharm
"""

# json数据格式的使用

import  json

# 把数据存储到json中
# filename = "myfile/num.json"
# numbers = [1,2,3,45,45,80]
# with open(filename,"a") as json_file:
#     json.dump(numbers,json_file)

# 读取json中的数据 json.load()

pathname = "num.json"
with open(pathname,"r") as f_obj:
    json_data = json.load(f_obj)
print(json_data)
