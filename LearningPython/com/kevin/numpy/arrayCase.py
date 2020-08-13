"""
@File    : arrayCase.py
@Time    : 2020/7/29 14:57
@Author  : KevinXiao
@Software: PyCharm
"""

import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# numpy数组的使用
a = np.array([1,2,3])
# 查看a的dtype类型
print(a.dtype)
print(a)
print(type(a))
# dtype数据元素的类型
# 浮点数的一维数组
b = np.arange(10,dtype=float)
print(b)
# 浮点数二维数组
d = np.array([[1,2,4],[4,5,6]],dtype=bool)
print(d)
c = np.arange(1,10,dtype=float)
print(c)



