dict1 = {'qwe': 100, 'asd': 890}
dict2 = dict(name='wang', agte=20)
print(dict1)
print(dict2)

##-----------------------------------

dict1 = {'qwe': 100, 'asd': 890}
dict2 = dict(name='wang', agte=20)
print(dict1['qwe'])
print(dict2.get('name'))
# 两种取值方式，但是区别是[]的方式是如果不存在的话会报错
# 但是get的形式如果不存在会显示none

dict1 = {'qwe': 100, 'asd': 890}
print(dict1.get('name', 'woai'))
# 这里表示的是如果这个key值不存在的时候，那么默认值就是后面的‘woai’

dict1 = {'qwe': 100, 'asd': 890}
print('name' in dict1)
dict1['name'] = 'qwe'  # 添加内容

del dict1['name'] # 删除

dict1.clear() # 清空操作

#---------------------------------------

dict1 = {'qwe': 100, 'asd': 890, 'name': 5500}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1)

# 输出结果会有区别
# dict_keys(['qwe', 'asd', 'name'])
# dict_values([100, 890, 5500])
# dict_items([('qwe', 100), ('asd', 890), ('name', 5500)])
# {'qwe': 100, 'asd': 890, 'name': 5500}

dict1 = {'qwe': 100, 'asd': 890, 'name': 5500}
keys1 = dict1.keys()
keys1List = list(keys1)
for k in keys1List:
    print(k)
# 将key值转化成列表的形式

dict1 = {'qwe': 100, 'asd': 890, 'name': 5500}
for item in dict1:
    print(item)
# 这里遍历也是只便利key值

dict1 = {'qwe': 100, 'asd': 890, 'name': 5500}
for item in dict1:
    print(item, dict1[item], dict1.get(item))
# 后面的两种方式都可以得到值

# key值不可以重复，但是value可以重复


items = ['fruit', 'book', 'price']
num1 = ['123', 'moyan', 'haogui']
dic1 = zip(items, num1)
print(list(dic1))
# 利用zip来将两个列表变成字典

items = ['fruit', 'book', 'price']
num1 = ['123', 'moyan', 'haogui']
d = {item: num for item, num in zip(items, num1)}
print(d)
##   字典生成式
d = {item.upper(): num for item, num in zip(items, num1)}
## 这样则变成大写
