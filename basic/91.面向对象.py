class Car:  # 封装属性
    def __init__(self, brand):
        Car.brand = brand

    def drive(self):
        print('汽车启动',self.brand)

car = Car('大众')
car.drive()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 这个属性不可以被外部直接调用把v

    def show(self):
        print(self.name, self.__age)


student = Student('asd', 12)
student.show()

#-------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名:', self.name, '年纪：', self.age)


class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, age, numberNum):
        super().__init__(name, age)
        self.numberNum = numberNum


student = Student('难', 123, '难')
teacher = Teacher('老师', 212, 1232343)
student.info()
teacher.info()
# 父类的调用，且支持多继承

#--------------------------------------------


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名:', self.name, '年纪：', self.age)


class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def info(self):  # 在子类中进行重写，就可以输出所有的数据了
        print('姓名:', self.name, '年纪：', self.age, '性别:', self.gender)

		def info(self):
        super().info()  # 用这种方式也可以调用
        print('gender:', self.gender)


class Teacher(Person):
    def __init__(self, name, age, numberNum):
        super().__init__(name, age)
        self.numberNum = numberNum

        def info(self):
            print('姓名:', self.name, '年纪：', self.age, '学号:', self.numberNum)


student = Student('难', 123, '难')
teacher = Teacher('老师', 212, 1232343)
student.info()
teacher.info()



#-----------------------------------------------


class Animal():
    def eat(self):
        print('animal need to ead')


class Dog(Animal):
    def eat(self):
        print('This is a dog')


class Cat(Animal):
    def eat(self):
        print('This is a cat')


class Person():
    def eat(self):
        print('The people need to eat')


def func(obj):
    obj.eat()


func(Animal())
func(Dog())
func(Cat())
func(Person())


# 多态，只要有eat方法，都可以调用

#----------------------------------------------



class Student():
    def __init__(self, name):
        self.name = name

    def __add__(self, other):  ######
        return self.name + other.name


stu1 = Student('李')
stu2 = Student('张')
s = stu1 + stu2
print(s)

# 调用add方法这样可以实现字符串的相加


#------------------------------------

# 浅拷贝：对象包含的子对象内容不拷贝
# 深拷贝：会拷贝对象中包含的子对象
