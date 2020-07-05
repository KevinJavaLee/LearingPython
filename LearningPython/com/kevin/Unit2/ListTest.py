"""
@File    : ListTest.py
@Time    : 2020/7/4 22:03
@Author  : KevinXiao
@Software: PyCharm
"""

# 列表的使用：
# 1.列表元素的访问
myList = ['anta','nike','adidas']
# 先输出列表
print(myList)
print(myList[0]) # 输出列表的第一个元素
print(myList[-1]) # 输出列表的最后一个元素

# 2.列表元素的修改、添加和删除
# 2.1 直接赋值修改
# 2.2 append() 在列表末尾增加元素
myList.append('rebook')
print(myList)
# 2.3 insert() 在列表中插入元素
myList.insert(0,'LiNing') # 在第一个位置插入元素
print(myList)

# 2.4删除元素 方法：pop() remove() del
del myList[0] # 删除第一个元素
print(myList)
carName = myList.pop() # pop()弹出末尾的元素，并且得到弹出来的值
print(carName)
print(myList)

# remove() 根据值删除元素
myList.remove('nike')
print(myList)

"""
总结：1.pop()和del的区别：
del 删除元素后 无返回值
pop()返回删除的值 实质为出栈
"""
print("#"*50)
# 3.组织列表
# 3.1使用方法sort()对列表进行永久性排序
car_List = []
car_List.append('bwm')
car_List.append('byd')
car_List.append('chery')
car_List.append('audi')
print(car_List)
car_List.sort()
print("after sorted car_List")
print(car_List)
# 3.2 使用sorted()对列表进行临时性排序
print(sorted(car_List, reverse=True))
print(car_List)
# 3.3 倒着打印列表
car_List.sort(reverse=True) # 
print(car_List)
# 3.4确定列表的长度
print(len(car_List)) # 列表的长度
# extend()方法的使用
print("#"*50)
print(car_List)
# 把其他列表增加到car_list中
motoBycircle = ['honda','wuyan']
car_List.extend(motoBycircle)
print(car_List)

# index() 求某个元素的索引位置 参数是可选的

# print(car_List.index('honda',0,4))# myList = [ value**2 for val in range(1,100,2)]

# count() 计算机某个元素在列表中出现的元素
print(car_List.count('honda'))

# 复试列表的方式
# 方式一：for 循环
# 方式二：
copy_carList = car_List[:];
print(copy_carList)
# 修改car_List中的元素
car_List[0] = 'wowo'
print(car_List)
print(copy_carList)
# 方式三：列表直接赋值
print("$"*50)
ref_carList = car_List
print(ref_carList)
print(car_List)
# 修改car_List
car_List[1] = '吉利'
print(ref_carList)
print(car_List)
# 两个指向一个列表
