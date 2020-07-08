"""
@File    : DefineClass.py
@Time    : 2020/7/8 11:31
@Author  : KevinXiao
@Software: PyCharm
"""

# 类的定义

class Person:
    # 属性
    name = '匡斯坦纳'
    age = 12

    # 方法的定义
    # 方法至少定义一个参数
    def sayHello(self):
        print("%s你好！"%self.name)

# 创建类对象
p = Person()
# 输出p的类型 id
print(type(p),id(p))
# 创建类的实例对象
p.sayHello()
# 创建第二个Person对象
p1 =Person()
# 修改类的属性
p1.name = '晓宇'
p1.sayHello()