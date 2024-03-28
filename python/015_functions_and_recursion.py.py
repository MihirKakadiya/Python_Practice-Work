


def percent(marks):
    p =  (sum(marks)/400)*100
    return p 

marks = [23,45,67,89]
avg1 = percent(marks)

marks2 = [83,95,67,89]
avg = percent(marks2)

print(avg1,avg)

# ...................................................

def greet(name):
    print("Good day," + name)

greet("mihir")#function calling............

# .........................................................

def mysum(n1,n2):
    return n1+n2+1

S = mysum(2,3)
print(S)

def greet(name="stranger"):   #defult parameter.............
    print("Hellow," + name)

greet("mihir")
greet()  #<------------------------------------

#recursion.................................

n = 5
p=1

for i in range(n):
    p = p*(i+1)
print(p)

def fect(n):
    p=1
    
    for i in range(n):
        p = p*(i+1)
    return p

f = fect(5)
print(f)

#recursion....................

def fectrec(n):
    if n == 1 or n ==0:
        return 1
    return n * fectrec(n-1)

f = fectrec(0)
print(f)


#1..............................

n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
n3 = int(input("Enter a number :"))

def biggest(n1,n2,n3):
    if n1>n2 :
        
        if(n1>n3):
            return n1
        else:
            return n3
        
    else:
        if(n2>n3):
            return n2
        else:
            return n3

m = biggest(n1,n2,n3)
print(m)

#2.................................

n = int(input("Enter a temp :"))

def temp(n):
    return (n * (9/5) )+ 32
c = temp(n)
print(c)
        
#3..................................

n = int(input("Enter a number :"))


def number(n):
    if  n == 0:
        return 0
    return n + number(n-1)
    
a = number(n)
print(a)

#4..............
n = int(input("Enter a number :"))

def pettern(n):
    for i in range(n):
         print("*" * (n-i))
    
a = pettern(n)
print(a)

#5.........................
    

n = int(input("Enter a number :"))

def cm(n):
    return n * 2.54

inch = cm(n)
print(inch)

#6....................................

s = "    hello mihir you are great   "
def remove(s,b):
    nstr= s.replace(b,"")
    return nstr.strip()
s = remove(s,"hello")
print(s)

#7.....................................

n = int(input("Enter a number :"))

def multiplication(n):
    i=1
    while i<=10:
        print(n*i)
        i = i+1

multiplication(n)




