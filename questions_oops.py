#Write a Python program to create a Student class and Creates an object to it. Call the method talk() to display student details
'''class student:
    def __init__(self) :
        self.name="raam"
        self.standard="6th"
        

    def talk(self):
        print(self.name,self.standard,self.marks)

s=student()
s.marks=300
s.talk()'''

#Program to demonistrate constructor will execute only once per object:
'''class Test:
    def __init__(self):
        #self.c="radhey"
        print("constructor execute")
    
    def talk(self):
        self.c="radhey"
        print("method ececute",self.c)

t=Test()
t1=Test()
t2=Test()
t.talk()
print(t.c)

#How to delete instance variable from the object:
class marks:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
       # del self.d

    def m1(self):
        pass
        
s=marks()
s.m1()
del s.c
del s.b
print(s.__dict__)

#How to access static variables: 
class student:
    marks=300
    def __init__(self):
        print(self.marks)
        print(student.marks)

    def m1(self):
        self.marks=500
        print(self.marks)
        print(student.marks)
    @classmethod
    def m2(cls):
        cls.marks=400
        print(cls.marks)
        print(student.marks)
        #cls.marks=400
    @staticmethod
    def m3():
        print(student.marks)

s=student()
print(s.marks)
print(student.marks)
s.m1()
s.m2()
s.m3()

#instance variable inside method
class test:
    def __init__(self):
        print("always win")
    def marks(self):
        self.phy=34
        self.che=45
        print(self.phy)
        #print(self.maths)
    def marks2(self):
        self.maths=42
        #print(self.maths)
        print(self.che)
s=test()
s.marks()
s.marks2()

print(s.phy)

#local variables
class test:

    def m(self):
        a=10

    def m2(self):
        b=20
        c=60
        print(c)
        #print(a)

s=test()
s.m()
s.m2()

#Program to track the number of objects created for a class: 
class test:
    count=0
    def __init__(self):
        test.count+=1

    @classmethod
    def cl_m(cls):
        print("the num of obj is",cls.count)

s=test()
s1=test()
s2=test()
s3=test()
s.cl_m()

#Passing members of one class to another class:
class Employ:
    def __init__(self,empno,empname,empsal):
        self.empno=empno
        self.empname=empname
        self.empsal=empsal
    def display(self):
        print("employ number",self.empno)
        print("employ name",self.empname)
        print("employ salary",self.empsal)
class test:
    def modify(self):
        self.empsal +=1000
        self.display()
s=Employ(18,"krishna",10000)
#test.modify(s)
#t=test()
test.modify(s)'''

#Duck typing
'''class bird:
    def sound(self):
        print("quack.quack...")

class aeroplane:
    def sound(self):
        print("sounds like fveeeee")

class rocket:
    def sound(self):
        print("sounds like zooo00m")

def sounds_off(self):
    self.sound()

sounds_off(bird())
sounds_off(aeroplane())'''
















































































