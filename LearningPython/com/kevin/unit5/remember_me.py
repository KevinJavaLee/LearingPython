"""
@File    : remember_me.py
@Time    : 2020/7/17 17:17
@Author  : KevinXiao
@Software: PyCharm
"""
import json
# 保存和读取用户生成的数据

# filename = "myfile\\username.json"
# usename = input("请输入用户的姓名：\n")
# with open(filename,'w') as json_obj:
#     json.dump(usename,json_obj)

# 读取用户的数据
# 如果用户名存储了就读取，否则就添加用户的姓名

pathname = "myfile\\username.json"
try:
    with open(pathname) as obj:
        usename = json.load(obj)
except FileNotFoundError:
    with open(pathname,'w') as obj:
        usename = input("请输入用户的姓名；")
        json.dump(usename,obj)
        print("欢迎用户："+usename)
else:
    print(usename)


