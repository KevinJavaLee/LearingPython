"""
@File    : InitClass.py
@Time    : 2020/7/8 11:38
@Author  : KevinXiao
@Software: PyCharm
"""

# 初试化类

class Person:
    # 初试化类
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f'{self.name}今年{self.age}')

p = Person('kuang',23)
p.sayHello()

# 修改属性
p1 = Person("xiaoyu",4)
p1.sayHello()
p1.age = 45
print(p1.age)
