"""
@File    : Project1.py
@Time    : 2020/7/24 9:50
@Author  : KevinXiao
@Software: PyCharm
"""

import  requests
from bs4 import BeautifulSoup
# 获取网址的内容
def getHTMLURL(url):
    try:
        req = requests.get(url,timeout=30)

        # 状态码不正常将抛出异常
        req.raise_for_status()
        # 编码
        req.encoding = req.apparent_encoding
        # print(req.text)
        return req.text
    except:
        return ""

#
def ConvertList(html,List):

    soup = BeautifulSoup(html,"html.parser")
    # 找出tbody的子孙节点
    # print(soup.find("tbody").children)
    # for tr in soup.find("tbody").children:
    #     tds = tr('td')
    #     print(tds)
    trs = soup.find_all("tr")
    for i in range(1,len(trs)):
        # print(trs[i].)
        tds = trs[i].find_all("td")
        List.append([tds[0].string,tds[1].string,tds[2].string])









def PrintList(UList,num):
    for i in range(num):
        u = UList[i]
        if u[2]== '福建':
            print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

# 主函数
def main():
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-2020.html"
    text = getHTMLURL(url)
    UniList = []
    ConvertList(text,UniList)
    # 调用输出函数
    PrintList(UniList,len(UniList))

if __name__ == '__main__':
    main()
