"""
@File    : iterateDictTest.py
@Time    : 2020/7/5 21:23
@Author  : KevinXiao
@Software: PyCharm
"""

person = dict(name = 'aircraft',sex='男',age='45')
# items()

dicts = person.items()
print(dicts)
# 遍历

# 遍历每一项
for i,j in dicts:
    print(i,j)
print("#"*50)
# keys() 遍历健值
for key in person.keys():
    print(key)

# values()
print("#"*40)
for value in person.values():
    print(value)