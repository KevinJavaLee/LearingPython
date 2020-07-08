"""
@File    : HiddenClass.py
@Time    : 2020/7/8 15:29
@Author  : KevinXiao
@Software: PyCharm
"""

# 不可从外部修改类内部的属性值
# class Person:
#
#     def __init__(self,name,age):
#         self.hiddenname = name
#         self.hiddenage = age
#
#     # 定义方法
#     def show(self):
#         print("调用show()方法")


# 创建Person类对象
# p = Person('晓宇',23)
# print(p)

# 改进型
class person:

    def __init__(self,__name,__age):
        self.__name = __name
        self.__age = __age

    # 定义方法
    def show(self):
        print("调用show()方法,",self.__age,self.__name)

p = person('匡总',23)
p.show()

