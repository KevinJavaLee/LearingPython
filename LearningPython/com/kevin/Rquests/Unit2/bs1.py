"""
@File    : bs1.py
@Time    : 2020/7/23 16:22
@Author  : KevinXiao
@Software: PyCharm
"""

# 遍历的方式

from bs4 import BeautifulSoup
import  requests

req = requests.get("http://python123.io/ws/demo.html")

# 获取文本
demo = req.text

soup = BeautifulSoup(demo,"html.parser")

# # 标签树的下行遍历
# print(soup.head)
# # 获取head的子节点
# print(soup.head.contents)

# 分隔符
print("#"*50)
# 获取body的子节点
# print(soup.body.contents)
# for by in soup.body.contents:
#     print(by)
#     print("#"*50)
#
# # 输出body的子节点个数
# print(len(soup.body.contents))
# # 获取最后一个子节点元素
# print("*"*100)
# print(soup.body.contents[1])

# 遍历儿子节点和子孙节点
# for chind in soup.body.children:
#     print(chind)
# print("#")
# for des in soup.body.descendants:
#     print(des)

## 上行遍历
# 得到
# print(soup.title)
# # 得到父类元素
# print(soup.title.parent)
# print("***")
# 得到所有的父类元素
# print(soup.title.parents)

# for par in soup.title.parents:
#     print(par)
#     print("*"*20)

# python的平行遍历
print()

print(soup.a.next_sibing)

print(soup.a.previous_sibling)

#
for atag in soup.a.next_siblings:
    print(atag)
    print("#")

#
for at in soup.a.previous_siblings:
    print(at)
    print("#")



