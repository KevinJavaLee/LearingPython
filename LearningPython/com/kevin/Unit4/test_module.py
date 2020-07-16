"""
@File    : test_module.py
@Time    : 2020/7/10 11:15
@Author  : KevinXiao
@Software: PyCharm
"""

# 在模块中，可以定义变量，在引入模块后就可以直接使用该变量
a = 10
b = 12

# 添加了_的变量则只能在内部被访问
_c = 15


# 调用方法
def show():
    print("这是show()函数")

print("测试此模块")