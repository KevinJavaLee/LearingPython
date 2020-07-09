"""
@File    : Inherient.py
@Time    : 2020/7/8 17:06
@Author  : KevinXiao
@Software: PyCharm
"""

class Animal:

    def __init__(self,name):
        self.name = name

    def run(self):
        print("动物正在跑")

    def sleep(self):
        print("动物正在睡觉")

    # 使用构造器
    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def read_name(self,name):
        self.name = name

# 继承Dog类继承Animal
class Dog(Animal):
    pass

# 调用类对象
a = Animal('匡总')
print(a.get_name)
a.run()
# 修改类的属性
a.name = '晓宇'
print(a.get_name)
# 子类建立对象
d = Dog('小匡')
d.sleep()

# 子类重写父类方法
print("#"*50)
#
class Cat(Animal):

    def __init__(self,name,age):
        # self.name = name
        # super()方法的使用
        super().__init__(name)
        self.age = age


    @property
    def get_name(self):
        return self.name
    @property
    def get_age(self):
        return self.age

    @get_name.setter
    def read_name(self, name):
        self.name = name

    @get_age.setter
    def read_age(self,age):
        self.age = age

    # 重写方法
    def sleep(self):
        print(f'{self.name}正在睡觉')

    #重写方法：
    def run(self):
        print(f'{self.name}正在跑步')

    # 增加自身的方法
    def eat(self):
        print(f'{self.name}正在吃东西')

c = Cat('晓宇',23)
print(c.get_age)
print(c.get_name)
c.sleep()
c.run()
c.eat()

