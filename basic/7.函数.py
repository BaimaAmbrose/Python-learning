def calc(a, b):
    c = a + b
    return c

result = calc(10, 20)
print(result)
# 新建函数以及函数的调用

def calc(a, b):
    c = a / b
    return c


result = calc(b=10, a=20)
print(result)
# 有两种传参数的方法

##-------------------

def fun(arg1, arg2):
    print("arg1:", arg1)
    print("arg2:", arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)


n1 = 2
n2 = [133, 23, 45, 2]
fun(n1, n2)
print(n1)
print(n2)

# 这里会发现最后的输出n2变化了，但是n1没有变化
# 这是因为n1是不可变化对象，而n2是可变化的
# 不可变对象在函数里改变，也不影响外面的值


#----------------------------------------

def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even


print(fun([12, 4, 2, 34, 76, 4, 23, 3, 2, 4]))

#---------------------------------------

def fun(a, b=10):
    print(a)
    print(b)


fun(100)
fun(50, 20) # 默认值

#----------------------------------------

def fun1(*argu): # 个数可变的位置参数
    print(argu)


def fun2(argu):
    print(argu)


fun1(10, 20, 30)
fun2(10)

def fun1(**argu): # 个数可变的关键字形参
    print(argu)

fun1(a=10, b=20, c=60)

#--------------------------------------

 def func(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)


lis = [123, 654, 22]
func(*lis)
dic = {'a': 22, 'b': 66, 'c': 990}
func(**dic)

#----------------------------------

def func():
    global age # 增加global，可以使函数内部变量变成全局变量
    age = 20

func()
print(age)

#-------------------------------

def fun(a):
    if a == 1:
        return 1
    return a * fun(a - 1)


print(fun(6))

#-------------------------

def fbn(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fbn(n - 1) + fbn(n - 2)


for i in range(1, 10):
    print(fbn(i))
## 斐波那契数列

#-------------------------------

lis = [{'rate': [9.9], 'id': 123, 'actors': ['大卫', '大王', '忠臣', ]},
       {'rate': [2.9], 'id': 170, 'actors': ['李雷', '小刘', '孙红', ]},
       {'rate': [3.9], 'id': 165, 'actors': ['王明', '宋小宝', '徐志摩', ]}, ]

name = input('输入你要查询的演员姓名:')
for item in lis:
    idTest = item['actors']
    if name in idTest:
        print(item['id'])`
