"""
@File    : Case1.py
@Time    : 2020/7/24 20:42
@Author  : KevinXiao
@Software: PyCharm
"""
import  requests
import re
# https://s.taobao.com/search?q=%E5%A4%A7%E6%95%B0%E6%8D%AE&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200724&ie=utf8
url = "https://s.taobao.com/search?q=大数据&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200724&ie=utf8"

def getHtmlText(url):
    try:
        kv = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        # req = requests.get(open(url))
        # req.raise_for_status()
        # print(req.status_code)
        # req.encoding = req.apparent_encoding
        with open(url,encoding = 'utf-8') as f :
            content = f.read()
        return content
    except:
        return "出现错误"



def getGoodInfo(goodList,html):
    try:
        price = re.findall(r'\"view_price\":\"[0-9]*.[0-9]*\"',html)
        title = re.findall(r'\"raw_title\":\".*?\"',html)
        for n in range(len(price)):
            pr = eval(price[n].split(":")[1])
            tr = eval(title[n].split(":")[1])
            print(pr)
            print(tr)
        print(price)
        print(title)
    except:
        pass
    # pass

def printGoods(goodLis):
    pass
def main():
    # url = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest"
    # url = "https://s.taobao.com/search?q=大数据&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200724&ie=utf8"
    url = "taobao.html"
    # 得到文本的内容
    html = getHtmlText(url)
    # print(html)
    print("结束")
    #
    goodList = []
    getGoodInfo(goodList,html)
    # # 打印商品信息
    # printGoods(goodList)
main()

