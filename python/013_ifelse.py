#elif....

a  = 26
if(a<2):
    print("hello")
elif(a>17):
    print("world")
elif(a<20):
    print("not greater")
else:
    print("not grater thaan 2 and 7")

#multiple if................

a  = 1
if(a>=10):
    print("greater")
if(a==17):
    print("world")
if(a>=20):
    print("greater")
else:
    print("not grater")

#...................................
age = int(input("enter your age : "))

if age>=18:
    print("YOur allowd")
else:
    print("not allowd")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

age = 18
if(age>=22 and age<=45):
    print("you are allowed")
else:
    print("not allowd")

#>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<
a  =  None

if(a is None):
    print("yes")

else:
    print("no")

#><><><><><><><><><><><><><><<><><<><><><<<>

b = [1,2,3,4]
print(2 in b)

#1_______________________________________{}

u1 = int(input("Enter z number :"))
u2 = int(input("Enter z number :"))
u3 = int(input("Enter z number :"))
u4 = int(input("Enter z number :"))

if (u1>u2):
    print(str(u1) + "  is Greatest")
elif (u2>u3):
    print(str(u2) + "  is Gretest")
elif(u3>u4):
    print(str(u3) + "  is gratest")
else:
    print(str(u4) + "  is greatest")

#2________________________

s1 = int(input("enter a marks of subject 1 : "))
s2 = int(input("enter a marks of subject 2 : "))
s3 = int(input("enter a marks of subject 3 : "))

if (s1<33 or s2<33 or s3<33):
    print("Fail")

elif (s1+s2+s3/3)<40:
    print("you are fail")

else:
    print("pass") 

#3......................................

comment = input("Enter text : ")

if("make money fast" in comment):
    spam = True

elif("buy now" in comment):
    spam = True

elif("click this" in comment):
    spam = True

elif("subscribe" in comment):
    spam = True

else:
    spam = False

if(spam):
    print("spam msg")
else:
    print("not spam")

# 4................

s = input("Enter string : ")
S = len(s)

if (S>10):
    print("Contain more than 10 characters")
else:
    print("Contain less than 10 characters")

#5........................

l = ["mihir","vatsal","zeel","parth","fenil"]

name = input("enter a name : ")

if  name in l:
    print("Youn are in <__>")
else:
    print("Sorry you are out >__<")

#6.............................

m1 = int(input("Enter marks of subject 1 : "))
m2 = int(input("Enter marks of subject 2 : "))
m3 = int(input("Enter marks of subject 3 : "))
m4 = int(input("Enter marks of subject 4 : "))

M = (m1+m2+m3+m4)/4

print(M)

if (M>90 and M<100):
    print("O grade")

elif (M>80 and M<90):
    print("A grade")

elif (M>70 and M<80):
    print("B grade")

elif (M>60 and M<70):
    print("C grade")

elif (M>50 and M<60):
    print("D grade")

elif (M<50):
    print("F grade")

#7.............................


comment = input("Enter text : ")


if("MIHIR" in comment):
    spam = True

elif("Mihir" in comment):
    spam = True

elif("mihir" in comment):
    spam = True

elif("M i h i r" in comment):
    spam = True

else:
    spam = False

if(spam):
    print(" YES !!! they talking about mihir")
else:
    print("NO they talking about someone else")
