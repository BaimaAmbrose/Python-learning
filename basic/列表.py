list1 = ['123', 123, 'asdqwr']
list2 = list(['123', 123, 'qwe'])
print(list1[0])
print(list1[-1]) # 这里的-1表示从后往前，-1也就是asdqwr
#   这两种方法都可以创建列表

#-----------------------------------------

list1 = ['123', 4567, 'wer', 'fuyop']
print(list1.index(4567, 1, 3))
# 这里表示搜索1到2，不包括搜索3

#--------------------------------------------
list1 = ['123', 4567, 'wer', 'fuyop', '4tytrereds', 'sdafahd', 'dfbvuj786']
print(list1[1:5:2])
# 这里也同样结尾是不包含第5个数据的，后面的2是取值间隔

#--------------------------------------------
list1 = ['123', 4567, 'wer', 'fuyop', '4tytrereds', 'sdafahd', 'dfbvuj786']
print(list1[5:1:-1])

#----------------------------------------------
list1 = ['123', 'esdfg', 6789]
list1.append(input('输入'))
print(list1)

#-------------------------------------------------

list1 = ['123', 'esdfg', 6789]
list2 = ['qwe', 'zxc']
list1.append(list2) #['123', 'esdfg', 6789, ['qwe', 'zxc']]
list1.extend(list2) #['123', 'esdfg', 6789, 'qwe', 'zxc']
print(list1)
# 这里发现append和extend不一样，append只能添加一个元素，所以这里将list2
# 当作了一个元素添加了进去，但是extend可以添加多个元素，所以是将list2里的元素分开添加

#--------------------------------------------

list1 = ['123', 'esdfg', 6789]
list1.insert(1, 90)
print(list1)

#-------------------------------------------
list1 = ['123', 'esdfg', 6789]
list2 = ['qwe', 'ertydfg', 'sd1']
list1[1:] = list2
print(list1)
# 这里用的是切片，将list1中从1开始的所有数据全部换成list2

#---------------------------------------------
list1 = ['123', 'qwefsad', 'fbgvdcf', '123']
print(list1)
list1.remove('123')
print(list1)
# remove只会删掉第一个元素

list1 = ['123', 'qwefsad', 'fbgvdcf', '123']
print(list1)
list1.pop(1)
print(list1)
# 这里是删除特定位置的元素
# 如果只写pop，就是栈弹出，删除最后一位元素

list1 = ['123', 'qwefsad', 'fbgvdcf', '123']
print(list1)
list1.clear()
print(list1)
# 清除元素

list1 = ['123', 'qwefsad', 'fbgvdcf', '123']
print(list1)
list1[1:3] = []
print(list1)
# 利用切片将1，2都删掉

del list1
# 删掉list1，然后就无法再输出了

#---------------------------------------------

list1 = ['123', 'qwefsad', 'fbgvdcf', '123']
print(list1)
list1[0] = '456'
print(list1)
list1[1:2] = ['156', '678546', '78tdfdf']
print(list1)
# 修改

#------------------Sort----------------------------

list1 = [345, 7568, 14354, 1, 8, 3, 99, 2]
print('排序前', list1)
list1.sort()
print(list1)

list1.reverse() # reverse只是单纯将数组反过来，如果想降序的话
list1.sort(reverse=True)
list3 = sorted(list1)  # 生成一个排序好的列表，但是是新的
list3 = sorted(list1, reverse=True) # 降序排序

list1 = [i for i in range(1, 10)]
print(list1)
# 利用for来给list赋值
list1 = [i + 1 for i in range(1, 10)]