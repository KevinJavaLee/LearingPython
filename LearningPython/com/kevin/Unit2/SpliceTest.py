"""
@File    : SpliceTest.py
@Time    : 2020/7/5 8:16
@Author  : KevinXiao
@Software: PyCharm
"""
# 切片的使用
squares = [1,32,5,4,9,5]
print(squares)
# 切片的使用
print(squares[:])

# 输出前三个元素
print(squares[:3])
print(squares[1:3])
#
# 没有指定结束的索引 ，则输出到最后
print(squares[0:])

# 没有指明开始缩影，则从索引位置 0 开始
print(squares[:3])

# 设置步长2 每隔1个输出一个
print(squares[::2])
# 从索引1开始，到索引5之前的一个索引位置结束，步长为3
print(squares[1:5:3])

# 倒着输出
print(squares[::-1])


# 切片改变列表的值
print("*"*20)
print(squares)
squares[0:3] = [23,45] # 将列表中前2个值修改为 23，45
squares[3:5] = [23,45,55] # 将索引位置  3，4 修改为23，45，并且增加一个元素
print(squares)
print("$"*20)
squares[1:3] = [15]
# 注意点：
print(squares)