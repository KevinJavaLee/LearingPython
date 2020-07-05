"""
@File    : forCase.py
@Time    : 2020/7/5 9:52
@Author  : KevinXiao
@Software: PyCharm
"""

letters = ['a','s','c','u','m']

# for循环遍历的使用

for w in letters :
    print(w,end="")

print()
# 加上切片一起的使用
for w in letters[::2] :
    print(w,end="")
# 遍历输出数字
print()
# range() 的使用

for i in range(10):
    print(i,end="")
print()
print("#"*20)
# 设置步长的长度，开始的元素
# 输出奇数

for i in range(1,100,2):
    print(i)

# 求一百以内每个奇数的平方
for j in range(1,100,2):
    print(j**2,end=" ")
# 用range()生成列表
# 分割前面的内容
print()
print("*"*50)

# 生成一个包含10的列表
squares = []
squares = list(range(1,10))
print(squares)

# 用for循环来实现
square = []
for d in range(1,100,2):
    square.append(d)
print(square)


print()
# 列表解析
myList = [value**2 for value in range(1,100,2)]
print(myList)

