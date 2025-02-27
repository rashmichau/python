#Inheritance in python
#Single level inheritance
'''class A:

    def feature1(self):
        print("work with feature1")

    def feature2(self):
        print("work with feature2")
class B(A):
    def feature3(self):
        print("work with feature3")

a=A()
b=B()
b.feature1()'''

# Multi level inheritance
'''class A:
    def feature1(self):
        print("work with feature1")

    def feature2(self):
        print("work with feature2")
class B(A):
    def feature3(self):
        print("work with feature3")

    def feature4(self):
        print("work with feature4")

class C(B):
    def feature5(self):
        print("work with feature5")

c= C()
b=B()  
c.feature1()
b.feature2()'''

# Multipal inheritance
'''class A:
    def feature1(self):
        print("work with feature1")

    def feature3(self):
        print("work with feature3 of class A")
class B:
    def feature3(self):
        print("work with feature3 of class B")

    def feature4(self):
        print("work with feature4")

class C(B,A):
    def feature5(self):
        print("work with feature5")

c=C()
c.feature3()
c.feature1()'''

# constructor behaves in inheritance,(MRO)method Resolution Order,use of super in inheritance
'''class A:
    def __init__(self):
        #super().__init__()    
        print("init in A")

    def feature1(self):
        print("work with A")

class B:
    def __init__(self):
       # super().__init__()
        print("init in B")
        
    def feature2(self):
        print("woek with the feature B")

class C(A,B):
    def __init__(self):
        super().__init__()   
        print("init in c")

    def feature3(self):
        print("work with feature of C ")

c=C()'''

#POLIYMORPHISM
#Operator overloading

'''class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2

        if r1>r2:
            return True
        else:
            return False

s1=student(98,92)
s2=student(95,93)
s3=s1+s2
print(s3.m1)
s3.m1=786
print(s3.m1)
s4=s1>s2
print(s4)
if s1>s2:
    print ("s1 is win")
else:
    print("s2 is win")'''

# class student:

#     name="radhey"
#     def marks(self):
#         print("marks of student")
    
#     @classmethod
#     def clasm(cls):
#         print("it is a class method")
    
#     @staticmethod
#     def stat():
#         print("it is a static method")

# s1=student()
# s1.clasm()
# s1.

'''class A():
    def __init__(self):
        self.name = "ravi"

class B:
    def __init__(self):
        self.name = "kavi"
        
    def print_name3(self):
        print(self.name)
    def setage(self,val):
        self.age=val

    def print_name(self):
        super().__init__()
        print(self.name)

    def print_name2(self):

        print(self.age)

obj = B()
obj.age=20
obj.print_name2()
# print(a)'''

#Program to overload multiplication operator to work on Employee objects:
'''class Employ:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    def __mul__(self,other):
        return self.days*other.sal
        

e=Employ("shivay",1000)
t=Timesheet("shivay",30)

print(t*e)'''

#method overriding
'''class Employ:
    def __init__(self):
        super().__init__()
        print("init in Employ")
    
    def creative(self):
        print("Employ creativity is good")

class student(Employ):
    def __init__(self):
       # super().__init__()
        print("init in student")

    def study(self):
        print("Enhance skills")
s=student()
e=Employ()
e.creative()'''




