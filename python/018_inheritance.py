

#$%..........................Single level inheritance................@#$%^

# class Employee:
#     company = "Google"

#     def getinfo(self):
#         print(f"Company name is {self.company}")
    
# class Programmer(Employee):
#     language = "python"

#     def getlan(self):
#         print(f"programmer language is {self.language} and he is working in {self.company}")

# e = Employee()
# p = Programmer()

# p.getinfo()
# p.getlan()

#..............................multiple...................

# class Employee:
#     company = "Vipro"
#     ecode=120


# class Freelancer:
#     company = "Google"
#     level=3

#     def upgradelevel(self):
#         self.level= self.level+1
    
# class Programmer(Employee,Freelancer):
#     language = "python"


# p = Programmer()

# p.upgradelevel()
# print(p.level)
# print(p.company)

#..................................multilevel........................


# class Person:
#     company = "Vipro"
    
#     def salary(self):
#         print("1000000")


# class Freelancer(Person):
#     company = "Google"

#     def alive(self):
#         print("I am alive also")
    
# class Programmer(Freelancer):
#     language = "python"

#     def getlanguage(self):
#         print(f"{self.language}")

# p = Person()
# f = Freelancer()
# pr = Programmer()

# p.salary()
# pr.salary()
# pr.alive()

#...super(). use for run child as well as perents class.................#

# super is use for constructor running syntax= super().__init()__

# class person:
#     comapny = "cello"
#     salary = 10000
#     bonus = 5000
#     location = "Surat"

#     @classmethod
#     def changesalary(cls, sal):
#         cls.salary=sal

#     @property
#     def totalbonus(self):
#         return self.salary + self.bonus

# p = person()
# print(p.salary)
# p.changesalary(20000)
# print(person.salary)
# print(p.totalbonus)

#1.............................................

from ast import increment_lineno
from operator import index
from re import I


# class c2dvector:

#     def __init__(self,i,j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"
    
    

# class c3dvectro(c2dvector):

#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

# v2d = c2dvector(1,3)
# v3d = c3dvectro(1,4,6)
# print(v2d)
# print(v3d)

#2............................................................

# class Animals:
#     animaltype = "Mammal"
# class pets(Animals):
#     color = "balck"
# class Dog(pets):
#     @staticmethod
#     def bark():
#         print("dog is barking bow bow")

# a = Animals()
# p = pets()
# d = Dog()
# d.bark()
# print(d.color)
# print(d.animaltype)

#3......................................................

# class employee:

#     salary = 10000
#     increment = 1.5

#     @property
#     def salaryafterincrement(self):
#         return self.salary*self.increment

#     @salaryafterincrement.setter
#     def salaryafterincrement(self,sai):
#          self.increment = sai/self.salary

# e = employee()
# print(e.salaryafterincrement)
# e.salaryafterincrement = 5000
# print(e.increment)

#4...................................................

# class number:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i

#     def __add__(self,c):
#         return number(self.real +c.real , self.imaginary+c.imaginary)
#     def __mul__(self,c):
#         mulreal = self.real*c.real-self.imaginary*c.imaginary 
#         mulimg = self.real*c.imaginary+self.imaginary*c.real 
#         return number(mulreal,mulimg)

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"

# c1 = number(1,5)
# c2 = number(8,5)
# print(c1*c2)
# print(c1+c2)

#5 how to represent a vector in python........................................................

class vector:

    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v = vector([1,2,3])
print(v)
        

        

#6........................................................


class vector:

    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index=0
        for i in self.vec:
            str1 +=f"{i}a{index} + "
            index +=1
        return str1[:-2]

    def __add__(self,vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)

    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += (self.vec[i] * vec2.vec[i])
        return sum

    def __len__(self):
        return len(self.vec)

v1 = vector([1,4,6])
v2 = vector([10,45,67])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))