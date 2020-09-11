"""
@File    : read_air.py
@Time    : 2020/9/4 19:51
@Author  : KevinXiao
@Software: PyCharm
"""


import  pandas as pd
import  numpy as np

data = pd.read_csv("air_data.csv",header=0)
# 删除多余的列

# print(data)
# # 排序
# aqi = data.groupby(by=["AQI"]).count()
# print(aqi)

# 排序
sort_data = data.sort_values(by=["AQI"],ascending=False)
print(sort_data[:20])
