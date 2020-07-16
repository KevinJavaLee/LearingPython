"""
@File    : Moudle.py
@Time    : 2020/7/9 10:26
@Author  : KevinXiao
@Software: PyCharm
"""


# 模块的使用
# 引用其他类的方法 类
# import 模块名 as 别名
# import可以在任何位置引用
# 多次引入包，但是只引用一次

import RefModule as m
#把一个模块中的所有东西引入到当前模块
from test_module import *
# 引入包文件
from module_file import a,b

m.test()
p = m.Pig(12,34)
print(p)
p.test_name()

#    在每一个模块内部都有一个__name__属性，通过这个属性可以获取到模块的名字
#   - __name__属性值为 __main__的模块是主模块，一个程序中只会有一个主模块

print(__name__)
print(m.__name__) # 在每一个模块内部都有一个__name__属性,通过这个属性可以获取模块的名字
print(m)
#
print("#"*50)
print(a)
print(b)
# 不可访问
# print(_c)
# 调用test_Module中的内容
show()

print()

# 输出module_file包中的模块a中num变量的值
print(a.num)
# 输出moudel_file包中模块b的变量

