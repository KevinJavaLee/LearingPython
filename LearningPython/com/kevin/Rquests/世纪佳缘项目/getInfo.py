"""
@File    : getInfo.py
@Time    : 2020/9/6 9:33
@Author  : KevinXiao
@Software: PyCharm
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
from multiprocessing.dummy import Pool as ThreadPool




# 定义请求头和数据
# 字典类型
data = {"sex":"f","key":"","stc":"1:43,2:18.99,3:155.170,23:1","sn":"default",
        "sv":"1","p":"1","f":"select","listStyle":"bigPhoto",
        "pri_uid":"258187106","jsversion":"v5"}
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
           "Referer": "https://search.jiayuan.com/v2/index.php?key=&sex=f&stc=1:43,2:18.99,3:155.170,23:1&sn=default&sv=1&p=1&pt=63&ft=off&f=select&mt=u",
            "Cookie": "guider_quick_search=on; accessID=20200903110553635709; _gscu_1380850711=99102365lhchlm15; Qs_lvt_336351=1599102382; stadate1=257187106; myloc=43%7C4304; myage=22; mysex=m; myuid=257187106; myincome=40; Qs_pv_336351=4533998924891422700%2C3707234980122493400; is_searchv2=1; SESSION_HASH=7c8f547cfdf3795c9b2aad4f42b30bc12b165d2d; jy_refer=www.baidu.com; FROM_BD_WD=%25E4%25B8%2596%25E7%25BA%25AA%25E4%25BD%25B3%25E7%25BC%2598; FROM_ST_ID=1764228; FROM_ST=.jiayuan.com; user_access=1; save_jy_login_name=18713837118; COMMON_HASH=99ffc52072a07337305f2cd465bee64a; sl_jumper=%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2020-09-03; last_login_time=1599355843; upt=Iq2cTfns3xemNMnaJPSW9sXnw838fxbDOH0PlwLlAdP0rGaHqoN%2AefmKoJq9tlPjMUaE6b9by8h3b%2AgN-YLEJ6nR; user_attr=000000; pop_1509508611=1599357045902; PROFILE=258187106%3A%25E4%25BD%25B3%25E7%25BC%2598%25E4%25BC%259A%25E5%2591%2598%3Am%3Aimages1.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10%3A3.0; pop_time=1599355876531; PHPSESSID=dc5bb78dd9ef5f190a6b469ea96cb8d8; pop_avatar=1; main_search:258187106=%7C%7C%7C00; RAW_HASH=yHelONqEyIpcZcXO9NQfKo9-8u44611QRWLpJ6ODeZADwykHJzCO-eYx6TTpUspdA6A0TKhgBLBpHzEf5hflCybUwg%2AbJOQM7jLg79r4%2ADBGu-g.",
           "Host": "search.jiayuan.com"

}

def getHtmlConten(url):
    try:
        req = requests.get(url,headers=headers)
        req.raise_for_status()
        req.encoding = 'unicode_escape'
        return req.text
    except Exception as e:
        print(e)

def getGrilsInfo(text):
    """
    提取有用的信息
    :param text:
    :return:
    """
    text = text.replace('\\','\\\\')
    data = json.loads(text,strict=False)
    # 获得用户的信息
    userinfo = data["userInfo"]
    # print(userinfo)
    # 遍历列表
    # 存储所有的人的信息
    userlist = []
    for user in userinfo:

        # 储存每一个人的信息
        ulist = []

        uid = user['uid']
        realUid = user['realUid']
        nickname = user['nickname']
        sex = user['sex']
        age = user['age']
        work_location = user['work_location']
        work_sublocation = user['work_sublocation']
        height = user['height']
        education = user['education']

        matchCondition = user['matchCondition']
        marriage = user['marriage']
        income = user['income']
        shortnote = user['shortnote']
        image = user['image']

        ulist.append(uid)
        ulist.append(realUid)
        ulist.append(nickname)
        ulist.append(sex)
        ulist.append(age)
        ulist.append(work_location)
        ulist.append(work_sublocation)
        ulist.append(height)
        ulist.append(education)
        ulist.append(matchCondition)
        ulist.append(marriage)
        ulist.append(income)
        ulist.append(shortnote)
        ulist.append(image)

        userlist.append(ulist)
    return userlist

def toCSVFormat(list):
    """
    主要用于将得到的列表内容保存到csv中
    :param list:
    :return:
    """
    try:

        data = pd.DataFrame(list)
        # print(data)
        # 转换成csv文件保存在本地
        # 不保存列名和索引
        data.to_csv("girls_info1.csv",mode="a",index=0,header=0)
    except UnicodeEncodeError:
        pass
    else:
        pass


def to_main(url):
    print(url+"开始下载！")
    content = getHtmlConten(url)
    users = getGrilsInfo(content)
    # for u in users:
    #     print(u)
    #     print("#"*50)
    print("url:"+"结束下载！")
    toCSVFormat(users)



def main():
    pool = ThreadPool()  # 双核电脑
    tot_page = []
    for i in range(9000,37036):
        url = "https://search.jiayuan.com/v2/search_v2.php?key=&sex=f&stc=2:18.99,3:140.260,23:1&sn=default&sv=1&p="+str(i)+"&pt=35027&ft=off&f=select&mt=d"
        tot_page.append(url)
    pool.map(to_main,tot_page)
    pool.close()
    pool.join()



if __name__ == '__main__':
    main()