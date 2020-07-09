"""
@File    : Inheritence.py
@Time    : 2020/7/8 20:37
@Author  : KevinXiao
@Software: PyCharm
"""

# 多重继承
class A(object):
    def test(self):
        print("这是A类的测试方法")

class B(object):
    def test(self):
        print("这是B类的测试方法")

# class C(A):
#     def test(self):
#         print("这就是C类的是测试方法")
# class D(B):
#     def test(self):
#         print("这就是D类的测试方法")
class E(A,B):

    print(A.__bases__)
    print(B.__bases__)
    print()
    pass

e  = E()
e.test()

