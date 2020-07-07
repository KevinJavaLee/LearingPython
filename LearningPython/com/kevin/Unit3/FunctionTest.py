"""
@File    : FunctionTest.py
@Time    : 2020/7/7 17:25
@Author  : KevinXiao
@Software: PyCharm
"""

# 高级函数的概念：
# 接收函数作为参数，或者把函数作为返回值
# 定义一个函数将列表中的偶数都保存到新的列表中

myList = [1,2,3,4,5,6,7,8,9]

# def produceList(myList):
#     newList = []
#     for w in myList:
#         if w % 2 == 0:
#             newList.append(w)
#
#     return newList

# 改进版 而且每个数大于5
# 写法1：
# def produceList(myList):
#     newList = []
#     for w in myList:
#         if w % 2 == 0 and w >= 5:
#             newList.append(w)
#
#     return newList


# 写法2：单独运用一个函数来判断列表中的数是否式偶数
# def produceList(m):
#     newList = []
#     # 定义函数判断该数是否式偶数
#     def isEeven(i):
#         if i % 2 != 0:
#             return True
#         return False
#     ##
#     for i in m:
#         if isEeven(i) and i > 5:
#             newList.append(i)
#
#     return newList

def produceList(m):

    # 定义函数判断该数是否式偶数
    def isEeven(i):
        if i % 2 != 0:
            return True
        return False
    ##
    if isEeven(m) and m > 5:
        return True
    return False



# 调用该函数
# filter()的使用：可以从序列中过滤掉符合条件的元素，然后返回一个新的元素
# 参数：函数 序列

# 定义筛选的函数
def fn(n):
    if n % 2 == 0:
        return True
    return False
# 返回值为一个新的序列,可迭代的结构
filterList = filter(fn,myList)
for i in filterList:
    print(i)
print(set(filterList))
print("#"*50)
list1 = filter(produceList,myList)
for i in list1:
    print(i)

# 匿名函数的使用
# Lambda表达式的使用
# 常规定义的函数
def sum (a,b ):
    return a + b
print("#"*50)
# 改用Lambda表达式
# lambda表达式用来创建一些简单的表达式
# lambda 参数，参数... :返回表达式

fn = lambda a,b:a + b
print(fn(2,3))

# 结合filter()的使用
print("#"*50)
lamSequence = filter(lambda i:i > 5 and i % 2==0 ,myList)
for l in lamSequence:
    print(l)

# map()对象 可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新的对象中
l = [1,5,67,66,89,14]

print("#"*50)
#
maps = map(lambda i:i**3,l)
# 遍历对象
for m in maps:
    print(m)

# sort() sorted()
# sort()该方法用来对列表进行排序
sortList = [9,3,5.4,6]
sortList.sort()
print(sortList)
# 对字符串进行排序
strList = ['12','kevin','xiaoyu','robert','alice','a']
strList.sort()
print(strList)
# key需要接收一个函数作为参数
strList.sort(key=len)
print(strList)
# sorted() 排序后不会对列表产生影响





