"""
@File    : Case.py
@Time    : 2020/7/8 15:15
@Author  : KevinXiao
@Software: PyCharm
"""

"""
练习：
    尝试自定义一个表示狗的类（Dog）      
        属性：
            name
            age
            gender
            height
            ...
        方法：  
            jiao()
            yao()
            run()
            ...
"""

class Dog:
    def __init__(self,name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    # 定义方法
    def shout(self):
        print(f'{self.name}正在汪汪大叫')

    def biting(self):
        print(f'{self.name}正在咬人')

    def run(self):
        print(f'{self.name}正在跑步！')

# 创建Dog 的对象
d = Dog('匡总',23,'male',150)
print(d.age)
print(d.name)
d.age = 25
print(d.age)
print(d)
# 调用方法
d.run()
d.biting()
d.shout()