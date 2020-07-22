"""
@File    : Case3.py
@Time    : 2020/7/22 21:00
@Author  : KevinXiao
@Software: PyCharm
"""

# 百度360搜索提交
import  requests

# 爬取地址
url = "http://www.baidu.com/s"
try:
    kv = {"wd":"python"}
    # 请求连接后接的参数
    req = requests.get(url,params=kv)
    req.raise_for_status()
except:
    print("出现异常")
else:
    if req.status_code == 200:
        print(req.text[:2000])