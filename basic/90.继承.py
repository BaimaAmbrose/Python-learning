class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"我的名字是{self.name}，我的年纪是{self.age}")

class Student(Person):
    def __init__(self,name,age,stuno):
        super().__init__(name,age)
        self.stunp = stuno

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.depertment = department

stu = Student("李雷",12,45354)
stu.show()
doc= Doctor("魍魅",43,"啥都学")
doc.show()

#——————————————————————————————————————————————————————————————————————————

class FatherA():
    def __init__(self, name):
        self.name = name

    def showA(self):
        print("A")


class FatherB():
    def __init__(self, age):
        self.age = age

    def showB(self):
        print("B")


class Son(FatherA, FatherB):
    def __init__(self, name1, age1, gender):
        FatherA.__init__(self, name1)
        FatherB.__init__(self, age1)
        self.gender = gender


son = Son("qwe", 123, "fff")
son.showB()
son.showA()
print(f"姓名是{son.name}，年纪是{son.age}，性别是{son.gender}")
# 这里调用的是name和age，而不是name1和age1，因为name1和age1是传入的值
# 所以调用的函数名称应该是和父类里一样的

#——————————————————————————————————————————————————————————————————————————

## 父类方法的重写
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"名字是{self.name}，年纪是{self.age}")


class Student(Person):
    def __init__(self, name, age, stuno):
        super().__init__(name, age)
        self.stuno = stuno

    # 改写父类里的数据
    def show(self):
        super().show()
        print(f"学号是{self.stuno}")


class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def show(self):
        print(f"名字是{self.name}，年纪是{self.age}，我的部门是{self.department}")


stu = Student("lisa", 12, 124123)
stu.show()

stu2 = Doctor("doctor", 32, "笑话")
stu2.show()

#--------------------------------------------------------------------

## 多态
class Person():
    def eat(self):
        print("eat food")


class Cat():
    def eat(self):
        print("eat fish")


class Dog():
    def eat(self):
        print("eat shit")


def fun(obj):
    obj.eat()


cat = Cat()
fun(cat)

#--------------------------------------------------------------------

## 重写str方法，使得在per调用这个函数的时候，输出的不再是地址，而是改写后的str方法
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "我让你返回这个"

per= Person("lilie",123)
print(per)

#--------------------------------------------------------------------

## 求圆的面积与周长

class Circle():
    def __init__(self, r):
        self.r = r

    def ger_area(self):
        return 3.14*pow(self.r,2)

    def get_permeter(self):
        return 2 * 3.14 * self.r


num = eval(input("input the r"))
cir = Circle(num)
print(f"area is {cir.ger_area()}")
print(f"permeter is {cir.get_permeter()}")

