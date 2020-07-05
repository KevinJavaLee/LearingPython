"""
@File    : MutableObject.py
@Time    : 2020/7/5 17:54
@Author  : KevinXiao
@Software: PyCharm
"""


myList = [i**2 for i in range(1,10)]
copy_List = myList

print(myList)
print(copy_List)
# 测量两个列表的地址值
print(id(myList))
print(id(copy_List)) # 两个指向同一个地址
# 修改其中一个的值
myList[0] = 100
print("after sorted list :")
print(myList)
print(copy_List)
print(id(myList))
print(id(copy_List))
# 结论：两个列表得地址并未发生改变
#

# 列表解析
copy_List = [value**3 for value in range(1,10,2)]
# 重新打印两个列表的值和地址
print(myList)
print(copy_List)
print(id(myList))
print(id(copy_List))

# is 和 == 的区别
# is 用于区分两个地址是否相同
# == 用来判断两个值是否相等
test_list = myList;
ref_list = [i**2 for i in range(1,10)]
print(test_list == myList)
print(test_list is myList)
print("#"*30)
print(test_list == ref_list)
print(test_list is ref_list)