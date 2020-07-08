"""
@File    : SetterAndGetter.py
@Time    : 2020/7/8 15:44
@Author  : KevinXiao
@Software: PyCharm
"""

# 可以通过setter()和getter()
class Pig:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    # 方法
    def getVolume(self):
        return self.weight * self.height

    # setter()
    def set_height_(self,height):
        self.height = height

    def set_weight_(self,weight):
        self.weight = weight

    # getter()

    def __getweight__(self):
        return self.weight

    def __getheight__(self):
        return self.height

p = Pig(10,20)
print(p.getVolume())
# 设置系的高度
p.set_weight_(50)
print(p.getVolume())

print(p.__getheight__())
print(p.__getweight__())
