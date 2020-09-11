"""
@File    : DownPic.py
@Time    : 2020/9/6 17:49
@Author  : KevinXiao
@Software: PyCharm
"""
# import urllib.request
import pandas as pd
import  requests
from multiprocessing.dummy import Pool as ThreadPool
import re

proxy = {}
def downPicture(url):
    initurl = url
    print("downing:"+url)
    try:
        req = requests.get(url, timeout=50)

        req.raise_for_status()

        name = str(url).split("/")[-1]
        path = "pic1/"+name
        with open(path,"wb") as f:
            f.write(req.content)
            f.close()

    except Exception as e:
        print(e)

    else:
        print(initurl+":结束！")

def main():
    # pool = ThreadPool(8)  # 双核电脑
    # tot_page = []
    data = pd.read_csv("pic_url_pro.csv",header=None,names=["名字","地址"])
    # data.drop_duplicates(inplace=True)
    data1 = data.reset_index(drop=True)
    name = data1["地址"]
    # print(name)
    for i in range(137,3025):
        print(name[i])
        # tot_page.append(name[i])
        # downPicture(name[i])
    # pool.map(downPicture, tot_page)
    # pool.close()
    # pool.join()
    # downPicture(name.values[0])

if __name__ == '__main__':
    main()
# https://hotpics.cc/wp-content/uploads/2020/08/Hot-nude-brunette-cutie-shaved-pussy.jpg
