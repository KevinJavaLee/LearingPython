"""
@File    : GetCityName.py
@Time    : 2020/9/4 16:01
@Author  : KevinXiao
@Software: PyCharm
"""
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# 得到所有城市的url,并且将其保存到一个列表中
def getCityName(text):
    soup = BeautifulSoup(text,"html.parser")
    # 找到id为citylist的标签
    cityList = soup.find(id="citylist")
    # 找到所有的a标签
    cities = cityList.find_all("a")
    dict = {}
    # 遍历输出
    for city in cities:
        # print("")
        # 得到所有的城市的网址
        city_url = city['href']

        # 得到该网址的内容
        city_content = city.string
        dict[city_content] = city_url

    return dict



# 得到Html的文本
def getHtmlText(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
        req.encoding = 'utf-8'
        return req.text
    except:
        print("出现错误！")

#

def toCsvList(content):
    # print(content)
    df = pd.DataFrame([content],index=["城市","网址"])
    # 转置
    new_df = df.T
    # 添加新的一列数据
    new_df['城市'] = new_df.index
    # 求出有多少行数据
    data_size = new_df["城市"].count()
    # print(data_size)
    # print(new_df)
    # # 生成列表
    new_df.to_csv("city_name.csv",index=0) # 不保存行索引

    # new_index = [i for i in range(1,data_size+1)]
    # new_df.reset_index()
    # new_df = pd.DataFrame(new_df)
    # print(new_df)
    # print(new_df.index)

def main():
    url = "http://www.air-level.com/"
    content = getHtmlText(url)
    city_list = getCityName(content)
    # print(city_list)
    toCsvList(city_list)
    # print(content)
if __name__ == '__main__':
    main()