"""
@File    : test.py
@Time    : 2020/7/22 17:20
@Author  : KevinXiao
@Software: PyCharm
"""

#  requests库的使用，爬取网页

import requests


# 用get的方法
r = requests.get("http://www.baidu.com")

# 连接的状态码
print(r.status_code)

# 返回当前文件编码
print(r.apparent_encoding)
# 设志返回文本的编码
r.encoding = "utf-8"
# 输出当前的编码方式
print(r.apparent_encoding)
# 输出文本
print(r.text)

#
print(r.json)

# 分割线
print("#"*50)
print(r.headers)