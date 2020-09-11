"""
@File    : pro_main.py
@Time    : 2020/9/6 21:17
@Author  : KevinXiao
@Software: PyCharm
"""

import pandas as pd

df = pd.read_csv("girls_sum.csv",header=None,names=["uid","realid","nickname","sex",
                                                    "age","work_location","work_sublocation",
                                                    "height","education","matchCondition","marriage","income"
                                                    ,"shortnote","image"
                                                    ])
print(df)
age = df.groupby(by="age").count()
print(age["uid"])
# df.drop_duplicates(inplace=True)
# df.reset_index(drop=True)
# # print(df[13][860:873])
# print(df[13])
# url_list=[]
# for i in range(930):
#     url = str(df[13][i])
#     # print(url)
#     new_url = url.replace("\/","/")
#     # print(new_url)
#     url_list.append(new_url)
# #
# ser = pd.Series(url_list)
# print(ser)
# print("#"*100)
# # print(str(df[13]).inplace(""))
# del df[13]
# # print(df)
# df[13]=ser
# print(df)
# df.to_csv("girls_sum.csv",header=0,index=0)
# print("结束")
