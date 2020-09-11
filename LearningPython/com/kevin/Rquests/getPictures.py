"""
@File    : getPictures.py
@Time    : 2020/8/13 13:27
@Author  : KevinXiao
@Software: PyCharm
"""

import requests
from bs4 import BeautifulSoup
import re #引入正则表达式库

root = "mypic/"




# 得到网页的内容
def getHtmlContent(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
        return req.text
    except:
        return "出现错误！"



# 得到每一页网页的连接地址
def getPageUrl(text):
    soup = BeautifulSoup(text,"html.parser")

    # 找到sub_main标签
    sub_main = soup.find(id="sub_main")
    movie_lists = sub_main.find_all(attrs={'class':'list_thumb'})
    for movie in movie_lists:
        movie_str= str(movie)
        # print(movie_str)
        url = re.findall(r'www.*jpg',movie_str)
        savePic(url[0])



# 把图片保存到本地
def savePic(url):
    try:

        http_url = "https://"+url
        req = requests.get(http_url,timeout=10000)
        # req.raise_for_status()
        path = root + url.split("/")[1]
        with open(path,"wb") as f:
            f.write(req.content)
            # 关闭文件
            f.close()
            print("文件保存成功！")
    except Exception:
        print("出现错误！")
    else:
        print("文件保存成功！")







def main():
    url_first = "https://en.kin8tengoku.com/listpages/all_"

    for i in range(0,75):
        url = url_first + str(i) + ".htm"
        # url = "https://en.kin8tengoku.com/listpages/type_529_1.htm"
        text = getHtmlContent(url)
        # print(text)
        getPageUrl(text)
        print(i)
        print("#"*50)
    pass

main()



