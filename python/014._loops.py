#.... While_loop.................
# i  = 1
# while i <= 50:
#     print(str(i))
#     i = i + 1

# print("done")

# l = ["apple","bananas","watermelon","grapes","mangos"]
# i=0
# while i<len(l):
#     print(l[i])
#     i = i + 1

#>>>>>>>>>>>.........for_loops.................>>>>>>>>>>>>>

# l = ["apple","bananas","watermelon","grapes","mangos"]

# for item in l:
#     print(item)

# range function >>>>>>>>>>>>>>>>>>

# for i in range(10):
#     if i == 5 :
#         continue
#     print(i)


# i = 5
# if i>0:
#     pass
# for i in range(10):
#     pass
# print("pass")

#1........................

# a = int(input("Enter a number : "))

# for i in range(1,11):
#     print(str(a) + "x" + str(i)+"="+str(i*a))

#2.........................
# l = ["mihir","vatsal","zeel","parth","fenil","mahir"]

# for name in l:
#     if name.startswith("m"):
#         print(f"hello{name}")

#3..........................
# a = int(input("enter a number  : "))
# i=1
# while i<=10:
#     print(f"{a}x{i}={a*i}")
#     i = i + 1

#4...........................prime number...........

# n = int(input("enter a number: "))
# Prime= True
# for i in range(2,n):
#     if(n%i == 0):
#         Prime= False
#         break
# if Prime:
#     print("THis number is prime")
# else:
#     print("this number is not prime")

#5......................................n natural number sum.

# a = int(input("Enter a natural number : "))
# i = 1
# b = 0
# while (i<=a):
#     b = b  + i
#     i = i + 1
# print(b)

# a = int(input("Enter a natural number : "))
# sum = 0 
# for i in range(1,a+1):
#     sum = sum + i
# print(sum)

#6........................fectorial serires.....
 
# a = int(input("Enter a number : "))
# f=1
# for i in range(1,a+1):
#     f = f * i
# print(f)

#7>>>>>>>>>>>>>>>>>pettern.

# n = 3

# for i in range(n):
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))
    

#8.....................

# n = 4

# for i in range(4):
#     print("*"*(i+1))

#9............

# n=3
# for i in range(n):
    
#     for j in range (n):
#         print(" * ", end="")
    
#     print()

#10..................
   
# a = int(input("Enter a number : "))

# for i in reversed(range(1,11)):
#     print(str(a) + "x" + str(i)+"="+str(i*a))
    


    
    







