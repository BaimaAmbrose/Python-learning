import math
print(math.pi)

from math import pi
print(pi)

# 第一种方法是导入所有的方法
# 第二种是只导入pi这个函数

#-------------------------

def add(a, b):
    return a + b
# 在一个文件中写入
# 然后在另一个文件中调用

import calc1
print(calc1.add(12, 2))

# 可以调用第一个文件中的方法
# 这里是模块

from calc1 import add
print(add(12, 3))

# 两种方法都可以

#-------------------------
#-------------------------
#-------------------------
# demo
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(10, 20))

#-------------------------
#-------------------------
#-------------------------

# demo2
import demo

print(demo.add(22,33))

# 这个代码的意思是只有当demo作为主程序的时候才会运行
# 而如果是从demo2处运行的话，那么代码就不运行

# 新建package包，新建程序imputA
a = 10

import package1.imputA as num1
print(num1.a)

# 引入包，然后调用
# from package1 import imputA
# from package1.imputA import a
# 这两种都可以导入


#-------------------------
#-------------------------
#-------------------------


file = open('abc.txt', 'r')
print(file.readline())
file.close()
# 打开abc文件，然后输出里面的内容

#---------------------------------
file = open('b.txt', 'w')
file.write('hello world')
file.close()
# 如果有文件则更新，如果没有文件则新建

#---------------------------------

file = open('b.txt', 'a')
file.write('hello world123')
file.close()

# 追加模式

#--------------------------------

file = open('abc.txt', 'r')
print(file.read())
# 读取模式，从头到位全都读出来
print(file.readline())
# 只读一行
print(file.readlines())
# ['飞机\n', '坦克\n', '大炮'] 每一行作为独立字符串放到列表里

#--------------------------------

file = open('abc.txt', 'a')
lst = ['as', 'we', 'fdss']
file.writelines(lst)
file.close()

#-----------------
file = open('abc.txt', 'r')
file.seek(2)
print(file.read())
file.close()
# 从第二位开始读入


# with 不需要手动关闭，不需要写close
with open('abc.txt', 'r') as f:
    print(f.read())
