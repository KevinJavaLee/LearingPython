"""
@File    : SetTest.py
@Time    : 2020/7/5 17:54
@Author  : KevinXiao
@Software: PyCharm
"""

# set的使用 集合是无序
# set的建立
squenceSet = {1,23,4,55,65}
# listSet = {[1,2,34,5],[12,344]}  可以通过set()来将序列和字典转换为集合
print(squenceSet,type(squenceSet))

# set()内放的应该是不可变集合：字符串，元组，
#  可以通过set()来将序列和字典转换为集合
mySet = set('hello')
mySet = set([1,2,4,6,7])
# 将字典转化为集合
dictSet = set({'name':123,'sex':'男'})
print(mySet)
print(dictSet)

# 集合方法的使用
# len()
mySet = set([1,2,3,4,56,66])
print(len(mySet)) # 长度为6

# x in s,s not in s
# 测试x是否在集合s中，

print(2 in mySet)
print(10 in mySet)
print("*"*50)
# add()方法向元素中添加元素
mySet.add(123)
mySet.add('kuangzon')
print(mySet)

print("#"*50)
# updata() 修改集合，从其他的中添加元素
mySet.update({'name':'kevin','sex':'man'})
mySet.update([3,4,45,6])
print(mySet)
# remove() 删除元素，如果没有该元素，则报错
mySet.remove('name')
print("deleted set :")
print(mySet)
print("#"*50)
# discard() 如果存在，则删除,
mySet.discard('name')
print(mySet)
# pop() 任意从结合中删除一个元素 如果集合为空，报错
mySet.pop()
print("poped set:")
print(mySet)

# clear() 删除集合的所有元素
