class Student: # 类的名字每个单词的首字母大写，其余小写
    native_place = 'Daqing'

		def __init__(self, name, age):
        self.nameme = name
        self.aggge = age

    def eat(self): # 称为方法
        print('学生在吃饭')

		@staticmethod
    def method(): # 静态方法
        print('调用静态')

    @classmethod
    def method2(cls): # 类方法
				print('调用类方法')

def drink(): # 称为函数
    print('喝水')


stu1 = Student(123,123)
stu1.eat() # 调用方法

stu2 = Student(123, 567)
print(stu2.nameme)
print(stu2.aggge) # 可以输入默认值并且调用

stu1 = Student(123,123)
Student.eat(stu1) # 这种方法也可以调用
# eat函数里因为有一个self，所以需要输入自身

print(Student.native_place)
Student.method2() # 调用类方法
Student.method() # 调用静态方法

stu2.gender = '女'
print(stu2.gender) # 也可以通过这种方式直接增加变量

def show():
    print('show调用')

stu1.show = show() # 将show函数变成stu1专属的方法
stu1.show
