"""
@File    : RegularExpression.py
@Time    : 2020/7/24 19:23
@Author  : KevinXiao
@Software: PyCharm
"""

# search()
import re
# 在一个字符串中搜索匹配正则表达式的第一个位置
match = re.search(r'[1-9]\d{5}',"BIT234567")

if match:
    print(match.group(0))


#
print("#"*50)
# match()方法的使用
match = re.match(r'[1-9]\d{5}',"234567hit")

# if match:
print(match.group(0))

# findAll()以列表的形式返回所有匹配的字符串

match1 = re.findall(r'[1-9]\d{5}',"123455hit, 288889xit")
print(match1)

# 将一个字符串按照正则表达式匹配结果进行分割
match2 = re.split(r'[0-9]\d{5}',"122333bit 234ti567890nit",1)
print(match2)
# 搜索字符串，返回一个匹配类型的迭代类型
match3 = re.finditer(r'[0-9]\d{5}',"122333bit 234ti567890nit")
for m in match3:
    if m:
        print(m.group(0))

# sub()在一个字符串替换所有匹配正则表达式的子串，然后返回结果
match4 = re.sub(r'[0-9]\d{5}',"kevin","234455hit,345bit345678")
print(match4)

# Re库的另外一种等价用法
pat = re.compile(r'[1-9]\d{5}')
reg= pat.search("kevin123456")
if reg:
    print(reg.group(0))


# Match()对象实例
mat = re.match(r'[0-9]\d{5}',"234455hit,345bit345678")
#.string输出带匹配的字符串
print(mat.string)
# 匹配时的pattern对象
print(mat.re)
# 开始匹配时的位置
print(mat.pos)
# 正则表达式搜索文本结束的位置
print(mat.endpos)
# .start匹配字符串在原始字符串的位置
print(mat.start())
# .end 匹配字符串在原始字符串结束的位置
print(mat.end())
#
print(mat.span())