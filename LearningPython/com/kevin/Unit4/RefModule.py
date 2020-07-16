"""
@File    : RefModule.py
@Time    : 2020/7/10 10:54
@Author  : KevinXiao
@Software: PyCharm
"""

class Pig:
    # 类变量
    count = 0
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
    def test_name(self):
        print(f'{self.weight}')

    def __str__(self):
        return "Pig[weight=%d,height=%d]"%(self.weight,self.height)


def test():
    print("这是一个test()方法")