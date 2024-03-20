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
