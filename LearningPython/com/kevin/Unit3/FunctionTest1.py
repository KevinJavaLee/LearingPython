"""
@File    : FunctionTest1.py
@Time    : 2020/7/7 21:17
@Author  : KevinXiao
@Software: PyCharm
"""

# 将函数作为返回值返回，也叫做闭包
def fn():

    def inner():
        print("这是内部函数")

    return inner

# 接收返回的函数
f = fn()
# 调用内部建立的函数
f()

# 闭包的示例2
# 闭包形成的条件：
#   1.函数嵌套
#   2.把内部函数作为返回值
#   3.内部函数必须使用外部函数的变量

# 统计列表的平均值闭包实例

def average():
    newList = []

    def computeAverage(num):
        newList.append(num)
        # 返回平均值
        return sum(newList) / len(newList)

    # 把内部函数作为返回值
    return computeAverage
# 调用函数
fn1 = average()
print(fn1(12))
print(fn1(14))
print(fn1(14))
print(fn1(16))

# 装饰器
# 希望能在在一个函数运行前后打印函数运行开始结束
def mul(a,b):
    return a+b

def divide(a,b):
    return a / b
def add(a,b):
    return a + b


print("#"*50)
# 方式一：
def newPrint(a,b):
    print("函数开始运行")
    r = add(a,b)
    print("函数运行结束")
    return  r
fn = newPrint(1,2)
print(fn)

print("#"*50)
# 方式二：
def new_add():

   def newFunc(a,b):
       print("函数开始运行")
       r = add(a,b)
       print("函数借宿运行")
       return r
    # 返回新建立的函数对象
   return newFunc

f1 = new_add()
print(f1(1,5))

def fn3():
    print("这个一个列子")
# 改进方式三：有些内部的函数每有参数

def new_fn3():

    def newFunc3():
        print("函数开始运行")
        fn3()
        print("函数结束运行")
    return newFunc3

# 调用函数
f5 = new_fn3()
f5()

# 改进用法
print("#"*50)
def begin_end(func):

    # *args表示接收的是所有的位置参数,元组
    # **kwargs表示接收的字典
    def new_obj(*args,**kwargs):
        print(args)
        print(kwargs)
        print("函数开始运行")
        result = func(*args,**kwargs)
        print("函数运行结束")
        return result

    return new_obj

f5 = begin_end(add)
f6 = f5(12,4)
print(f6)
#
F1 = begin_end(fn3)
print(F1())

#
print("#"*50)

@begin_end
def new_func():
    print("正在编程")

new_func()






