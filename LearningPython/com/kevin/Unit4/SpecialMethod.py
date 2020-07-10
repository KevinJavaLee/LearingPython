"""
@File    : SpecialMethod.py
@Time    : 2020/7/9 9:45
@Author  : KevinXiao
@Software: PyCharm
"""

# 特殊方法的使用
class Person:
    # 特殊方法相当于java中的构造器
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # python定义的特殊垃圾回收方法，主要在垃圾回收之前调用
    def __del__(self):
        pass

    # 相当于java中的toString()方法
    def __str__(self):
        return "Person[name=%s,age=%d]"%(self.name,self.age)
    #
    # def __repr__(self):
    #     print("")
    def __repr__(self):
       return "hello"
    def __hash__(self):
        return hash(self.name,self.age)
    # 类似于Java类继承Comparable接口重写compare()
    def __lt__(self, other):
        return self.age > other.age
    # 通过__bool__()来指定对象转换为布尔值

    def __bool__(self):
        if self.age >= 18:
            return True
        return False

"""
object.__lt__(self, other) x<y
object.__le__(self, other)x<=y
object.__eq__(self, other)x==y
object.__ne__(self, other)x!=y
object.__gt__(self, other)x>y
object.__ge__(self, other)x>=y
"""
# 建立Person实例对象
p = Person('kevin',24)
print(p)
# print(repr(p))
print(repr(p))
#
print("#"*50)
p1 = Person('robot',3)
p2 = Person('robot',10)

print(p1.__lt__(p2))
print(p1 > p2)
print(p2 > p1)

if p1:
    print("已成年")
else:
    print("未成年")