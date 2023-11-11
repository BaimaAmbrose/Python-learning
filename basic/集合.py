# 是没有value的字典，所以里面不可以有重复的值
# 是无序的

s1 = set(range(0, 11))
print(s1)
# set 表示集合

s1 = set([1, 3, 5, 3, 32, 1]) # 列表
print(s1)

s1 = set('python')
print(s1)

s1 = set((1, 45, 23, 34, 2, 1)) # 元组
print(s1)

s1 = set({1, 5, 32, 21, 2, 1}) # 集合
print(s1)

s1 = {1, 5, 32, 21, 2, 1}
print(s1, type(s1))

s1 = set()# 这样生成的才是空集合
s1 ={} # 这样系统会默认是dict类型

s1.add('qwe')
s1.update({'eew', 1, 6, 43, 1}) # 添加元组
s1.update(['eew', 1, 6, 43, 1]) # 添加列表
s1.update(('eew', 1, 6, 43, 1)) # 添加集合

s1.remove(1)
s1.discard('qwe') # 区别在于discard如果删除不存在元素，是不会报错的
s1.pop() # 删除任意元素
s1.clear() # 清空

s1 = {1, 3, 4, 2}
s2 = {1, 2, 3, 4}
print(s1 == s2) # 判断相等，不看元素顺序

print(s2.issubset(s1)) # s2是s1的子集
print(s1.issuperset(s2)) # s1是s2的父集
print(s1.isdisjoint(s2)) # 没有交集为true，有交集为false

print(s1.intersection(s2)) # 求两者的交集
print(s1 & s2) # 也是求交集
print(s1.union(s3)) # 求并集
print(s1 | s3)
print(s1.difference(s2)) # s1中的元素删掉s2
print(s1 - s2)
print(s1.symmetric_difference(s2)) # 两边不同的元素全都求出来
print(s1 ^ s2)

lis1 = {i * i for i in range(9)} # 集合生成式