class number:
    def sum(self):
        return self.a + self.b

num = number()

num.a =12
num.b =34
s = num.sum()
print(s)

a =12
b =34

print("sum of a nd b is", a+b)

class Employee:
    company= "Tesla"
    salary= 500000 #class attribute

spike = Employee()
mihir = Employee()

spike.salary = 600000 #instance attribute
print(spike.salary)
print(mihir.salary) #class attribute

#....................self.......................

class Employee:
    company= "Tesla"
    def getsalary(self):
        print(f"Salary of this employee is {self.salary} in comapany {self.company}")

spike = Employee()


spike.salary = 600000 
spike.getsalary()

#......................static................

class Employee:
    company= "Tesla"
    def getsalary(self):
        print(f"Salary of this employee is {self.salary} in comapany {self.company}")
    
    @staticmethod
    def greet():
        print("Hello sir, Good morning")

spike = Employee()


spike.salary = 600000 
spike.getsalary()
spike.greet()

#.................constructor....................

class Employee:
    company= "Tesla"

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary= salary
        self.subunit = subunit
        print("Employee is created")
    
    def getdetails(self):
        print(f"the name is {self.name}")
        print(f"the salary is {self.salary}")
        print(f"the company is {self.subunit}")
        
    def getsalary(self):
        print(f"Salary of this employee is {self.salary} in comapany {self.company}")
    
    @staticmethod
    def greet():
        print("Hello sir, Good morning")

spike = Employee("Spike",100,"Google")
spike.getsalary()
spike.greet()
spike.getdetails()

#1..................................

class Programmer:

    company = "Google"

    def __init__(self,name,product):
        self.name = name
        self.product= product

    def getinfo(self):
        print(f"comanap is {self.company} and programmer name is {self.name} and working on {self.product} ")


spike = Programmer("Mihir","Map")
MIhir = Programmer("ZEEL","YT")
spike.getinfo()
MIhir.getinfo()

#2......................................

a = int(input("Enter a number : "))

class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"Squre is {self.number * self.number}")
    def cube(self):
        print(f"cube is {self.number **3}")
    def root(self):
        print(f"Squreroot is {self.number **0.5}")

b = Calculator(a) 
b.square() 
b.cube()
b.root()  


#4..................................

a = int(input("Enter a number : "))

class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"Squre is {self.number * self.number}")
    def cube(self):
        print(f"cube is {self.number **3}")
    def root(self):
        print(f"Squreroot is {self.number **0.5}")

    @staticmethod
    def greet():
        print("Good Morning Folks !!!")

b = Calculator(a) 
b.greet()
b.square() 
b.cube()
b.root() 


#5..........................

class train:
    def __init__(self,name,status,fair):
        self.name = name
        self.status = status
        self.fair = fair
    def getinfo(self):
        print(f"name of train is {self.name}")
        print(f"seats availabe in train is {self.status}")
        print(f"fair of train is {self.fair}")
    
    def bookticket(self):
        if(self.status>0):
            print("you can book ticket")
            self.status = self.status-1
        else:
            print("pls try in tatkal")

garibrath = train("Garibrath",90,300)

garibrath.getinfo()
garibrath.bookticket()
garibrath.getinfo()
        


    

