"""
@File    : Garbage.py
@Time    : 2020/7/9 9:34
@Author  : KevinXiao
@Software: PyCharm
"""

# 方法没有被调用就是垃圾

class A(object):
    def __init__(self,name):
        self.name = name

    # python的垃圾回收机制
    # __del__特殊方法，在正式被调用前被回收
    def __del__(self):
        print("正在回收垃圾！")

a = A("kevin")
b = a
print(b.name)
a = None # 没有任何对象对a进行引用所有a 就变成了垃圾
#
b = None




