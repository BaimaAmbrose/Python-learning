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
