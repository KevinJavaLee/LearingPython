"""
@File    : BeatifulSoup1.py
@Time    : 2020/7/23 15:41
@Author  : KevinXiao
@Software: PyCharm
"""

from bs4 import BeautifulSoup
import  requests

req = requests.get("http://python123.io/ws/demo.html")
# print(req.text)

# 把返回的内容赋值给一个变量
demo = req.text

# 解析返回的内容
# 传入要解析的内容和解析器
soup = BeautifulSoup(demo,"html.parser")
# print(soup.prettify())

# BeautifulSoup的基本元素

# 访问网页的标签内容
# tag = soup.head
# # print(soup.head)
# # 返回标签的属性
# print(tag.attrs)
# # 返回标签的名字
# print(tag.name)
# # 返回标签中间的内容
# print(tag.string)
# # 返回标签中注释的内容
# print(tag.comment)

print("#"*50)
# 返回body内容
# print(soup.body)
# print(soup.body.p)

# Tag的属性
tag_a = soup.a
# 获取tag的属性
print(tag_a)
# 获取所有的属性
tag_attr = tag_a.attrs
print(tag_attr)
# 获取单一的属性值
print(tag_attr['href'])
# 进行遍历
for att in tag_attr:
    print(att+":"+str(tag_attr[att]))

