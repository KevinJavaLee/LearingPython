"""
@File    : FunctionParam.py
@Time    : 2020/7/6 17:57
@Author  : KevinXiao
@Software: PyCharm
"""

# 位置参数 值参数 可变参数

# 函数的参数
# 位置参数
# 实参传递给形参的数一一对应
def sum(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

sum(1,2,3)

# 关键字参数可以不按照一一对应的顺序
def difference(a=1,b=2,c=3):
    print("a-b-c",a-b-c)
# 如果不传参数，则会使用默认值
difference()
print("#"*50)
difference(1,3)
difference(1,3,6)

# 关键字参数和位置参数的联合使用
# 位置参数应该放在关键字参数之前
# 混合使用关键字和位置参数时，必须将位置参数写到前面
difference(1,3,c=10)
difference(1,b=4)

print("#"*50)
# 在函数中对参数进行赋值
def changeVal(c):
    c[0] = 10
    print(c)

list = [1,2,3]
print(list)
changeVal(list)
print(list)
list1 = [1,2,3]
print("#"*50)
print(list1)
changeVal(list1[:])
print(list1)

