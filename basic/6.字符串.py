str = 'abcdefgc'
print(str.index('c')) # 查询第一次出现的位置，如果不存在会报错
print(str.rindex('c')) # 查询最后一次出现的位置，不存在会报错
print(str.find('c')) # 查询第一次出现的位置，不存在显示-1
print(str.rfind('c')) # 查询最后一次出现的位置，不存在显示-1

#------------------------------------------

str = 'i wanNa fuCking aNymOre'
print(str.upper()) # I WANNA FUCKING ANYMORE
print(str.lower()) # i wanna fucking anymore
print(str.swapcase()) # I WANnA FUcKING AnYMoRE
print(str.capitalize()) # I wanna fucking anymore
print(str.title()) # I Wanna Fucking Anymore

#--------------------------------------------

str = 'hell'
print(str.center(10, '*')) # 十个单位居中，各填充*
print(str.ljust(10, '@')) # 左对齐
print(str.rjust(10, '@'))
print(str.zfill(10)) # 左边填充0

#------------------------------------------

# 字符串的拆分
str = 'what the fucking day'
print(str.split()) # ['what', 'the', 'fucking', 'day'] 默认根据空格
str2 = 'what|the|fucking|day'
print(str2.split(sep='|')) # ['what', 'the', 'fucking', 'day']
print(str2.split(sep='|', maxsplit=1)) # 设定最大分割次数
# ['what', 'the|fucking|day']
print(str2.rsplit(sep='|', maxsplit=1)) # 从右侧开始区分

#----------------------------------------

str = "whatsthat"
print(str.isidentifier()) # 判断是否为合法表示符，不包括空格和标点
print('\t'.isspace()) # 是否全由空白字符组成
print(str.isalpha()) # 是否全由字母组成
print(str.isdecimal()) # 是否全由十进制数字组成
print(str.isnumeric()) # 是否全由数字组成
print(str.isalnum()) # 是否全由数字和字母组成

#----------------------------------------

str = 'what are you doing'
print(str.replace('what', 'how')) # 字符串的替换
print(str.replace('what', 'how', 2)) # how how what are you doing 替换两次
lis = ['what', 'is', 'that']
print('a'.join(lis))# whataisathat
lis = ('what', 'is', 'that')
print(''.join(lis)) # 元组也一样可以使用

print('|'.join('replace')) # 也可以直接使用字符串
# r|e|p|l|a|c|e

#---------------------------------------------

# 字符串的比较
str1 = 'qwe'
str2 = 'qwer'
print(str1 < str2) # 比较符 >,>=,<,<=,==,!=

#--------------------------------------------
# 字符串的拆分
s = 'hello,world'
s1 = s[:5]
s2 = s[6:] # 从第六位开始切
se = '!'
print(s1)
print(s2)
print(s1 + se + s2)
# hello
# world
# hello!world
print(s[1:8:2]) # el,o
print(s[::-1]) # dlrow,olleh
print(s[-5::1]) # world

#-------------------------------------------

name = input('name:')
age = int(input('age:'))
print('我的名字是%s，我今年%d岁' % (name, age)) # 利用占位符来拼接

name = input('name:')
age = input('age:')
print('我的名字是{0}，我今年{1}岁，我的儿子也叫{0}'.format(name, age))
# 利用花括号来做占位
print(f'我的名字是{name}，我今年{age}')

#--------------------------------------

print('%10d' % 99) # 宽度为10
print('%.3f' % 3.13123123)
print('%10.3f' % 3.13123123) # 既保证宽度又保证精度

#----------------------------------------

print('{0:.3}'.format(3.13213123)) # 3.13
print('{0:.3f}'.format(3.13213123)) # 3.132
