"""
@File    : 线性规划.py
@Time    : 2020/8/25 16:55
@Author  : KevinXiao
@Software: PyCharm
"""
import numpy as np
# import cvxopt as cp
import cvxpy as cp
import pandas as pd

# 读取数据
d1 = pd.read_excel("./dataset/Pdata5_6.xlsx",header=None)
# print(d1)
# 获取所有的值
d2 = d1.values
# print(d2)
# 所有的数据
c = d2[:-1,:-1]

# 最后一行数据

d = d2[-1,:-1].reshape(1,-1)

# 最后一列数据

e = d2[:-1,-1].reshape(-1,1)
#

x = cp.Variable((6,8))
print(x)

print("#"*50)
print("d:")
print(d)
print("#"*50)
print("e:")
print(e)
# print("#"*50)
# print(c)
# print("#")

# 构造目标函数
obj = cp.Minimize(cp.sum(cp.multiply(c,x)))
# 构造约束条件
con = [cp.sum(x,axis=1,keepdims=True)<=e,cp.sum(x,axis=0,keepdims=True)==d,x>=0]

# 构造模型

prob = cp.Problem(obj,con)

# 求解模型
prob.solve(solver="GLPK_MI",verbose=True)

#
print("最优值为：",prob.value)

#
print("最优解为：",x.value)






