print(123)
print('helloworld')
print(3+1)

#新建文件并且写入字符，a+的含义，如果文件没有就创建，如果有文件的话，那么就在文件里面进行追加
fp = open('/Users/baima/Desktop/newWorld.txt', 'a+');
print('helloworld', file=fp)
fp.close()

#所有输出在单行里
print('hello', 'world', 'python')

##-------------------转义字符----------------------

print('hello\nworld') # 这里的\n表示的是换行-newline，前后字符是不同的一行

print('hello\tworld')
print('helloo\tworld')
print('hellooo\tworld')
print('helloooo\tworld')
#这里一个\t表示一个制表位，一个制表位是4个字符，如果前面的字符刚好满足四个以内，那么就不会生成新的
#但是如果是四个，那么就会新建一个新的制表位，\t是水平制表符

print('hello\rworld') #这里的\r表示回撤，所以输出后就只有 world

print('hello\bworld') #这里的\b表示back，回撤一位，所以输出就只有 hellworld

print('我说\'大家好\'') #这里的反斜线就表示这里的单引号不是字符，而是我要输出的内容

print(r'hello\nworld') #前面的r表示后面的转义字符不起作用，所以最后的输出结果是 hello\nworld

## print(r'hello\nworld\')  #要注意的是这里字符串的结尾不可以是反斜杠

print(r'hello\nworld\\') #但是可以是两个反斜杠

name = 'qwe'
print(name)
print(id(name)) #表示标识
print(type(name)) #表示类型

##------------------数据类型---------------------

print(0b11101) # 0b 表示二进制，输出显示十进制结果
# 0o 表示八进制，0x表示十六进制

#float 会存在计算不精确的情况
print(1.1 + 2.2) #3.3000000000000003
print(1.1 + 2.1) #3.2

#这里需要引入模块decimal(十进制，小数)
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2')) #这里得到的结果就是正确的

# python中的true和false可以转换为整数，true是1，false是0
print(True + 1) #2 但是这里开头一定要注意大写

# 这里使用三引号里面的内容可以换行，但是如果只有一个的话不可以
senc = '''qwe
123qwe'''
print(senc)

# 数据类型转换
name = '阿基鲁尔夫特'
age = 123
print('name' + name + 'age' + str(age))

#这里的数据转换，如果是float可以转换为int，但是会失去小数点后面的数字
#如果是str类型，str类型里本身是整数，是可以转换的
#如果str类型里本身是小数，那么会报错
n1 = '123'
n2 = '123.2'
n3 = 123.2
print(int(n1))
print(int(n2)) #会报错
print(int(n3))

# input　入力の函数です
word = input('これはなんですか')
print(word)

#ここで注意して、input後、このnum１の種類はstrです、
#それで、直接に足し算をするなら、結果は１２です
#int()が使うなら、結果は３です
#strの種類は足し算することができない
num1 = input('数を入力してお願い')
num2 = input('もう一度数を入力してお願い')
print(int(num1) + int(num2))
#直接に数の種類を変えるならもいいです
num1 = int(input('数を入力してお願い'))
num2 = int(input('もう一度数を入力してお願い'))
print(num1 + num2)

print(1 + 2) #足し算　たしざん
print(1 - 2) #引き算　ひきざん
print(1 * 2) #掛け算　かけざん
print(5 / 2) #割り算　わりざん
print(5 // 2) #割り切る　わりきる
print(5%2) #余り　あまり
print(2**2) #2の2乘です　じょう
print(-9 // 4) #数が正または負の場所、結果は下に切り捨てられる、結果は−３です
print(-9 % 4) #余り=割られる数ー割れる数*割り算　-9-4*-3=3
print(9 % -4) #9-(-4)*3=-3

a, b, c = 10, 20, 30
print(a, b, c) #文字が数を連続的に代入して　もじ・れんぞく

#数が交換して　こうかん
a, b = 10, 20
a, b = b, a
print(a, b)

#isはidを比較するの文字です
a = 10
b = 10
print(a is b) # true


#bool 运算符
#or and
a = 10
b = 10
print(a == 10 and b == 10)#True
print(a == 10 and b < 10)#False
print(a == 10 or b < 10)#True
print(not a == 10 or b < 10)#False

# in と　not in
a = 'helloworld'
print('w' in a)#True
print('q' not in a)#True

a = 4
b = 5
print(a & b)
#这里看的是二进制，
#100
#101
#只有都为1的时候结果为1，所以最后结果是100，也就是4
#如果是100和001的话，那么结果就是0

a = 4
b = 1
print(a | b)
#同理，或，这里结果是5
print(4 << 1) #二进制左移一位，结果是8

#运算符优先级
#算数运算符>位运算符>比较运算符>布尔运算符
#python里的所有对象都有一个bool值
#以下的对象bool值都是False
#False，数值0，None，空字符串，空列表，空元组，空字典，空集合

##-------------if/else/elif-------------------

money = 2000
takeMoney = int(input('取りたい金額を入力してお願い'))
if money >= takeMoney:
    money = money - takeMoney
    print('成功して、余り金額は：', money)
else:
    print('失敗して')
#--------------------------------------------------------
num = int(input('数を入力してお願いします'))
if num % 2 == 0:
    print(num, 'が偶数です')#ぐうすう
else:
    print(num, 'が奇数です')#きすう
#--------------------------------------------------------
num = int(input('input the score please'))
if 100 > num >= 90:
    print('perfect')
elif 90 > num > 60:
    print('great')
else:
    print('just so so')
#--------------------------------------------------------
member = input('Are you member')
money = int(input('the price of total shop'))

if member == 'true':
    if money > 200:
        print('打五折')
    else:
        print('打七折')
else:
    if money > 200:
        print('打八折')
    else:
        print('不打折')
#--------------------------------------------------------
num_a = int(input('第一の数を入力して'))
num_b = int(input('第二の数を入力して'))
print((num_a, '大于', num_b) if num_a > num_b else (num_b, '大于', num_a))

num_a = int(input('第一の数を入力して'))
num_b = int(input('第二の数を入力して'))
print(str(num_a) + '大于' + str(num_b) if num_a > num_b else str(num_b) + '大于' + str(num_a))

##-------------range-----------------------

r = range(10)
print(r)
print(list(r)) #这里的range表示从0到10。只有当是list的时候，才可以输出0——9的数字

r2 = range(10,20)
print(list(r2)) #输出10到19

r3 = range(10,20,5)
print(list(r3)) #输出10，15

##--------------------while-----------------

num = 1
while num < 10:
    print(num)
    num += 1


# 求0到100的偶数和
a = 1
sum1 = 0
while a <= 100:
    if a % 2 == 0:
        sum1 += a
    a += 1
print(sum1)

##--------------------for--------------------

for num1 in range(11):
    print(num1)

#--------------------------------
for str in 'stanger':
    print(str)

#---------------------------------
for _ in range(5):
    print('I love you anymore')
# 输出五次这句话

#--------------------------------
sumNum = 0
for num in range(101):
    sumNum += num
print(sumNum)

sumNum = 0
for num in range(101):
    if num % 2 == 0:
        sumNum += num
print(sumNum)


#-----------------------------------------

for num in range(100, 1000):
    a = 0
    zennbuSUM = 0
    dannsuSUM = 1
    for suu in str(num):
        for _ in range(3):
            dannsuSUM *= int(suu)
        zennbuSUM += dannsuSUM
        dannsuSUM = 1
    if zennbuSUM == num:
        print(zennbuSUM)

# 153
# 370
# 371
# 407
#-----------------------------------------
for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    sumNum = ge ** 3 + shi ** 3 + bai ** 3
    if item == sumNum:
        print(item)

#--------break----------

for num1 in range(100):
    if num1 == 50:
        break
print(num1)
#-----------------------------
num1 = 0
while num1 < 100:
    num1 += 1
    if num1 == 10:
        break
print(num1)
#---------- ---------------------------

password = 1234
passFlag = 0
for num1 in range(3):
    inputPASSWORD = int(input('input the password'))
    if inputPASSWORD == password:
        print('the password is right')
        passFlag = 1
        break
    else:
        print('the password is wrong')
if passFlag == 0:
    print('input the password are three times already, you cannot try it again')

#--------continue------------

for item in range(1, 51):
    if not item % 5 == 0:
        continue
    print(item)

#----------else--------------

for num1 in range(5):
    if num1 == 3:
        print(num1)
        break
else:
    print(998)
#  这里的else的用处就是遇到break的时候，else本身也不执行了

password = 1234
for item in range(3):
    passwordInput = int(input('input the password'))
    if passwordInput == password:
        print('password is right')
        break
    else:
        print('password is wrong, input again please')
else:
    print('Sorry, you cannot try it again')

#  这里可以用一种更方便的方式来执行，而不需要像之前那样写一个表示符

#---------嵌套循环-------------

for num1 in range(1, 10):
    for num2 in range(1, 10):
        print(str(num1) + '*' + str(num2) + '=' + str(num1 * num2), end='\t')
    print()

# print的结尾写 end='\t' 则输出不换行