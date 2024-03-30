#bydefult mode is read
#w is for overwriting and a is for adding contant
from asyncore import read
from importlib.resources import contents


a = open('first.txt', 'r')#use to open and read contant of files....

data = a.readline()#read first line
print(data)

data = a.readline()#read second line
print(data)

a.write("spike is appending")
a.write("spike is writing")

a.close()

with open('s.txt', 'r') as s:
    a = s.read()

with open('s.txt', 'w') as s:
    a = s.write("me")

#1................................

f = open('s.txt', 'r')

data = f.read()
print(data)

if 'twinkle' in data:
    print('yes')
else:
    print("no")

f.close()

#2..................................
def game():
    return 948

score = game()

with open ('sample.txt', 'r') as f:
    a = f.read()

if a == '':
    with open ('sample.txt', 'w') as f:
        f.write(str(score))


elif int(a)<score:
    with open ('sample.txt', 'w') as f:
        f.write(str(score))

#4............................
with open('s.txt','r')as  f:
    content = f.read()

content = content.replace("shit","#$$%^$")

with open('s.txt','w')as  f:
    f.write(content)

#5............................
words = ["shit","spike","hello"]
with open('s.txt','r')as  f:
    content = f.read()

for word in words:

    content = content.replace(word,"#$$%^$")

    with open('s.txt','w')as  f:
        f.write(content)

#8...........
with open('s.txt','r')as f:
    content = f.read()

with open("copy.txt",'w')as f:
    f.write(content)

#10...............

with open('copy.txt','w') as f:
    f.write("")

#11..............................

import os
old = "copy.txt"
new= "new.txt"

with open(old)as f:
    content = f.read()
with open(new,'w')as f:
     f.write(content)

os.remove(old)




    
    






