"""
@File    : Rectangle.py
@Time    : 2020/7/8 16:26
@Author  : KevinXiao
@Software: PyCharm
"""

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    #
    @property
    def get_width(self):
        return self.width

    @property
    def get_height(self):
        return self.height

    @get_width.setter
    def set_width(self,width):
        self.width = width

    @get_height.setter
    def set_heigth(self,height):
        self.height = height




    def getArea(self):
        return self.width * self.height


r =  Rectangle(12,234)
print(r.getArea())
r.height = 20
print(r.getArea())

# 调用方法改为调用对象
r.set_heigth = 50
r.set_width = 100
print(r.get_height)
print(r.get_width)
print(r.getArea())
