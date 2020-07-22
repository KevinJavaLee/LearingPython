"""
@File    : ERROR.py
@Time    : 2020/7/22 19:21
@Author  : KevinXiao
@Software: PyCharm
"""

# 爬虫的通用框架
import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.encoding = r.apparent_encoding
        # 如果状态不是200，将引发异常
        r.raise_for_status()
        print(r.headers)
    except:
        print("出现错误！")
    else:
        if r.status_code == 200:
            return r.text

if __name__ == "__main__":
    url = "http://www.baidu.com"
    text = getHTMLText(url)
    print(text)
