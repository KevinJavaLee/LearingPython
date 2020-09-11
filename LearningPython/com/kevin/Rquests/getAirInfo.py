"""
@File    : getAirInfo.py
@Time    : 2020/9/4 17:55
@Author  : KevinXiao
@Software: PyCharm
"""



import pandas as pd
url = "http://www.air-level.com"

# print(air_data)
# 首先读取数据
def readCityInfo():
    data = pd.read_csv("city_name.csv")
    web = data["网址"]
    # print(web)
    return web



def getUrlInfo(text):
    try:
        air_data= pd.read_html("http://www.air-level.com/air/beijing/", header=0, encoding='utf-8')[0]
        # print(text.count())
        size = text.count()
        # print(text[1])
        for i in range(1,size):
            # 求出地址
            myurl = url + text[i]
            # 得到数据
            data = pd.read_html(myurl,header=0,encoding="utf-8")[0]
            # 合并数据
            air_data = pd.concat([air_data,data])
            print(i)
        # 重置索引
        air_data.reset_index(drop=True)
        air_data.to_csv("air_data.csv",na_rep='NaN')
        print(air_data)
        return air_data
    except Exception:
        print("出现错误")







def main():
    web = readCityInfo()
    getUrlInfo(web)

if __name__ == '__main__':
    main()

    pass