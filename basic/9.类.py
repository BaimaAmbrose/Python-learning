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

#-----------------------------------------------------------
# 私有的类

class Car():
    def __init__(self, brand, color, size):
        self._brand = brand  # 受到保护，只能本类和子类去使用
        self.__color = color  # 受到限制，只能本类去使用
        self.size = size  # 全都可以使用

    def _def1(self):
        print("子类和本身可以使用")

    def __def2(self):
        print("只有本身可以使用")

    def def3(self):
        self._def1()
        self.__def2()
        print(self._brand)
        print(self.__color)


car = Car("BYD", "red", "15")
car.def3()
print(car._brand) # 这里可以输出
print(car.__color)  # 这里会报错，出了类的定义范围就无法使用
car._def1() # 这里可以输出
car._def2() # 这里会报错
# 如果想要访问，需要按照一下的样式来写
print(car._Car__color)
car._Car__def2()

#————————————————————————————————————————————————————————————

class Student():
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property # 使其在外部可以调用
    def age(self):
        return self.__age

    @age.setter # setter方法使其可以在外部进行修改
    def age(self,value):
        if value> 100 or value < 0:
            print("the age is wrong")
        else:
            self.__age =value


stu = Student("asd", 123)
print(stu.name, ",her age is", stu.age)
stu.age = 21
print(stu.name, ",her age is", stu.age)


#————————————————————————————————————————————————————————————

