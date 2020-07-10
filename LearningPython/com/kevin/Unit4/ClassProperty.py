"""
@File    : ClassProperty.py
@Time    : 2020/7/9 8:46
@Author  : KevinXiao
@Software: PyCharm
"""

# 类属性和类方法 、静态方法
# 实例属性和实例方法

class creatrure:

    # 类属性
    count = 0
    cntNum = 0
    def __init__(self,name):
        self.name = name
        # 每创建一个对象cntNum加1
        creatrure.cntNum += 1

    @property
    def get_name(self):
        return  self.name
    @get_name.setter
    def set_name(self,name):
        self.name = name

    # 实例方法
    def test(self):
        print("这是实例方法")

    # 类方法的使用

    @classmethod
    def testClass(cls):
        print("这是一个类方法")

    # 静态方法的使用
    # 一般用作工具类
    @staticmethod
    def staticMethod():
        print("这是一个静态方法")


# 测试类变量和实例变量
c = creatrure(12)
c1 = creatrure(12)
c2 = creatrure(12)
# 通过对象访问类变量
print(c.count)
print(creatrure.count)
# 分别通过类对象和实例对象修改类属性
c.count = 10
print(c.count)
print(c1.count)
creatrure.count = 100
print(creatrure.count)
print(c.count)
print(c1.count)
print(c2.count)
# 类属性只能通过类.属性类改变 实例属性无法改变

# 类方法和实例方法的使用
# 类对象调用实例方法，需要手动传入参数
# 实例对象调用会调用第一个参数
creatrure.test(c)

# 类对象调用类方法
creatrure.testClass()
# 实例对象调用类方法
c.testClass()

# 结论：类对象和实例对象都可以调用实例方法，没有区别

"""

"""


