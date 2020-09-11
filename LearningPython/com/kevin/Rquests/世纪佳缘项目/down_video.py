"""
@File    : down_video.py
@Time    : 2020/9/7 11:19
@Author  : KevinXiao
@Software: PyCharm
"""


import requests
from bs4 import BeautifulSoup

headers = {
    'cookie': "bs=1kfg8xrm4urlktibwj1see2s7gxv8ull; ss=416954180971255585; _ga=GA1.2.328524346.1593437024; APUnique2_3=2286329247; platform_cookie_reset=pc; fg_9d12f2b2865de2f8c67706feaa332230=84889.100000; lang=cn; platform=pc; ua=0d7547ea912e3ce2a35572c8b9a755b1; _gid=GA1.2.384990218.1599447854",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

def getHtmlContent(url):
    try:

        #
        print("开始")
        req = requests.get(url,headers=headers)
        req.raise_for_status()
        with open("pic1/01.mp4","wb") as f:
            f.write(req)
            f.close()
    except Exception as e:
        print(e)




url = "https://ev.phncdn.com/videos/202007/09/331463202/1080P_4000K_331463202.mp4?validfrom=1599445066&validto=1599452266&rate=50000k&burst=50000k&hash=nXXAJ6%2BwDZ%2Bx0kXEtdRvpCQgs3k%3D"
getHtmlContent(url)