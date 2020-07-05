"""
@File    : DictTest.py
@Time    : 2020/7/5 17:54
@Author  : KevinXiao
@Software: PyCharm
"""

#
# 字典的健可以是任意的类型 值则只能是任意不可变的对象
#
alines = {'name':'superkuang','sex':'男'}
print(alines)
# 得到值 根据健来获取值
print(alines['name'],alines['sex'])
print("#"*50)
# 1.字典的创建
# 使用dict()来创建字典
person = dict(name = 'aircraft',sex='男',age='45')
print(person)

# 双值序列来创建字典
human = dict([('name','kuang'),('sex','男')])
# len()计算出字典的长度
print(human,type(human),len(human))

# 方式三：创建字典类型
female = dict({'name': 'xiaohong','age':23})
print(female)

# 修改字典的值，存在则覆盖
female['name'] = 'jyw'
# 如果不存在，则添加该元素到字典中
female['sex'] = '女'
print(female)
print("#"*20)
# 如果该健存在，则返回该健所对应的值。否则插入默认值，或者要插入的数,默认值为None
female.setdefault('info')
print(female)
female.setdefault('email','6666')
print(female)
# del d(key) 删除字典中的值
print("#"*50)
print(female)
# 删除健为age的项
del female['age']
print(female)


# get()根据健来获取值，没有则返回None
print(female.get('kuang'))

print("#"*50)
# update()将其他的字典中的key-value添加到字典中，如果有重复的key,则后面的value替代前面的
girls = dict({'a':'c','d':'e'})
female.update(girls)
print(female)
woman = dict({'a':'d'})
female.update(woman)
print(female)
# pop()的使用:如果关键字在字典中，则删除该关键字和返回这个值，否则返回默认值，如果默认值没有，则报错
print(female.pop('a')) # 返回关键字
print(female.pop('d','e')) #female中不存在关键字d,则返回默认值e
# print(female.pop('d')) # 报错


# popitem()返回和删除一对键值对 如果字典为空则报错
print("#"*50)
print(female)
female.popitem()
print(female)

# copy()浅复制
people = female.copy()
print(people)
# 把健为'info'的改为一个键值对
people['info'] = {'name':'superkuang'}
print(people)
print(female)

d = dict({'a':{'name':'kaung'},'b':'c'})
d1 = d.copy()
print(d)
print(d1)
print("#"*50)
d1['a']['name'] = 'xiaoyu'
print(d,id(d))
print(d1,id(d1))



# clear()的使用 清空字典
female.clear()
print(female)


