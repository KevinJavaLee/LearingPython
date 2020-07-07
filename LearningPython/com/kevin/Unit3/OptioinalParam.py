"""
@File    : OptioinalParam.py
@Time    : 2020/7/7 9:21
@Author  : KevinXiao
@Software: PyCharm
"""

# 可变参数
# 不定长参数
# 定义一个函数，求多个书之和
#  *形参只能接收位置参数，而不能接收关键字参数
def sum(*nums):
    result = 0
    for num in nums:
        result += num
    print(result)
#
sum(1,3,5,6,7)
sum(12,34,55,66,7)

# 在定义函数时，可以使用在形参前加一个*，这个形参会获得所有的实参
def fn(*a):
    print(type(a))

fn()

# 带*参数的形参只能够有一个，可以和其他参数混合使用
def sumMultiply(a,b,*c):
    result = 0
    for val in c:
        result += val
    sum = 0
    sum = result * (a + b)
    return  sum
val = sumMultiply(1,2,4,5,6,7)
print(val)
# 可变参数不是必须写在最后，带*参数后的所有参数，必须以关键字形式的参数传递
print("#"*50)

def fn1(a,*b,c):
    print("a=",a,type(a))
    print("b=",b,type(b))
    print("c=",c,type(c))

fn1(1,2,3,45,c=10)

# 如果带*参数放在第一位，则其后的参数必须使用关键字参数
def fn3(*a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

fn3(1,3,4,c=1,b=2)
# 要求传递的所有的参数必须是关键字参数
print("#"*50)
def fn4(*,a,b):
    print("a=",type(a))
    print("b=",type(b))
fn4(a=1,b=6)
print("#"*50)
# **形参可以接收其他的关键字参数，它会将这些参数统一保存到一个字典中
# **形参只能有一个，且只能放在最后
def fn5(a,b,**c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

fn5(b=1,a=12,c=456,d=7898)
# 参数的解包
print("#"*50)
def fn6(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

t = (7,8,9)
# 可以在序列中加一个*号，会把元组中的数据一一解析到对应的参数
fn6(*t)
print("#"*50)
# 通过**对字典进行解析
# 通过**来对一个字典进行解包操作
t1 = {'a':100,'b':200,'c':300}
# 字典中的健应该与函数中的参数相对应
fn6(**t1)