"""
@File    : FotmatTest.py
@Time    : 2020/7/3 16:17
@Author  : KevinXiao
@Software: PyCharm
"""

# 格式化符号的使用
# %s %d
money = 100.9
name = '匡总'
num = 10
# money保留小数点后两位
print("%s卖了%03d件东西，赚了%.2f" % (name,num,money))
# 格式化符号的高级使用
# f'{}'
age = 23
count = 12
NickName = '晓宇'
print(f'{NickName}今年{age+1}岁，已经得到了{count -1 }')