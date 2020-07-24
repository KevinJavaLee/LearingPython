"""
@File    : test.py
@Time    : 2020/7/24 10:59
@Author  : KevinXiao
@Software: PyCharm
"""

# CrawUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        kv = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        r = requests.get(url, timeout=30,headers=kv)
        # r.raise_for_status()
        print(r.status_code)
        r.encoding = r.apparent_encoding
        with open("uni.html","wb")as f:
            f.write(r.content)
        return r.text
    except :
        return "出现错误"


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-2020.html'
    html = getHTMLText(url)
    print(html)
    # fillUnivList(uinfo, html)
    # printUnivList(uinfo, 20)  # 20 univs


main()