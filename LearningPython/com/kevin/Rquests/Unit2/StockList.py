"""
@File    : StockList.py
@Time    : 2020/7/27 14:46
@Author  : KevinXiao
@Software: PyCharm
"""

import requests
from bs4 import BeautifulSoup
import re

# 得到网页内容
def getHtmlContent(url,code = "utf-8"):
    try:
        kv = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
              }
        req = requests.get(url,headers=kv)
        req.raise_for_status()
        req.encoding = code
        return req.text
    except:
        return ""


# 主要功能得到所有的股票代码，并将其放入到列表中
def getStockList(slist,stockUrl):
    html = getHtmlContent(stockUrl,"UTF-8")
    print(html)
    # 放入BeautifulSoup库中
    soup = BeautifulSoup(html,"html.parser")
    # 找到所有的a标签，提取其中的地址
    atags = soup.find('tbody')
    soup.find()
    print(atags)
    # 遍历的到的a标签
    # for a in atags:
    #     try:
    #         href_url = a.attrs['href']
    #         print(href_url)
    #         print()
    #     except:
    #         print("出现错误！")
    #
    # #
    # return list
# 得到所有的骨片信息将其存入于列表中
def getStockInfoList(ilist,infoUrl):
    pass


def main():
    stock_list_url = "http://quote.eastmoney.com/center/boardlist.html#boards-BK07071"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    outputFile = "stock.txt"
    sList = []
    iList = []
    getStockList(sList,stock_list_url)
    # getStockList(iList,stock_info_url)

if __name__ == '__main__':
    main()
    print("运行结束")

