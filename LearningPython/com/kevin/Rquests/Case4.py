"""
@File    : Case4.py
@Time    : 2020/7/22 21:05
@Author  : KevinXiao
@Software: PyCharm

"""

# 从网上下载图片
import requests
import os

#
url = "http://img0.dili360.com/ga/M01/48/E0/wKgBzFmyTcaACuVKACZ-qAthuNY888.tub.jpg@!rw9"
root = 'mypic/'
# try:
#     req = requests.get(url)
#     req.raise_for_status()
#     # 把得到文件内容写到
#     path = "mypic\\01.jpg@!rw9"
#     with open(path,"wb") as f:
#         f.write(req.content)
#         print("文件")
#         f.close()
# except:
#     print("出现错误！")

#

path1 = root + url.split("/")[-1]

if not os.path.exists(root):
    os.mkdir(root)
if not os.path.exists(path1):
    req = requests.get(url)
    with open(path1,"wb") as f:
        f.write(req.content)
        f.close()
        print("文件保存成功！")
else:
    print("文件已经存在！")
# except:
#     print("出现错误！")


