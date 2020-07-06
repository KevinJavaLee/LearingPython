"""
@File    : CaculateSet.py
@Time    : 2020/7/6 16:45
@Author  : KevinXiao
@Software: PyCharm
"""

MySet = set([1,3,4,6,5,9,80])
refSet = set([1,3,4,6,5,9,80])
# set <= other issubset
print(MySet <= refSet) # 是否set集合中的每一个元素都在另外一个集合中
print(MySet < refSet) # set <= other and set != other
print(MySet.issubset(refSet))

# union() 或者 |
# set | other |  相当于属于中的U
copySet = set([9,3,4,10,12,45])
print(refSet | copySet)

# set & other 相当于数学中的交

print(refSet & copySet)

# set - other - ... 返回在set中且每在other中的集合
# difference
differenceSet = refSet - copySet
differenceSet1 = refSet.difference(copySet)
print(differenceSet)
print(differenceSet1)

print("#"*50)
print(refSet)
print(copySet)
# set ^ other 相当于 symmetric_difference() 即出现在set 中，也出现在other中，当不都共同出现
commonSet = refSet ^ copySet
commonSet1 = refSet.symmetric_difference(copySet)
print(commonSet)
print(commonSet1)

