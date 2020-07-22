"""
@File    : Case1.py
@Time    : 2020/7/22 19:38
@Author  : KevinXiao
@Software: PyCharm
"""

# 案例一：爬取京东页面信息
import  requests

# 爬取地址
url = "https://xiaomi.world.tmall.com/shop/view_shop.htm?spm=a21bo.2017.201863-1.d1.5af911d9BiobtS&user_number_id=1714128138&pvid=bb5eec7d-bf72-4c1b-ab68-e7a77dc37e82&pos=1&brandId=3506680&acm=03014.1003.1.765824&scm=1007.13143.56636.100200300000000"
try:
    req = requests.get(url,timeout= 30)
    req.raise_for_status()
except:
    print("出现异常")
else:
    if req.status_code == 200:
        print(req.text)


