# d = {"Mihir":"is great",
#     "Spike": "is good",
#     "List": [1,2,3,4,5],
#     "Name": {'SPIKE' : 'MIHIR'}}

# print(d['Mihir'])
# print(d['Spike'])
# print(d['List'])
# print(d['Name']['SPIKE'])
# #changable,unordered

# #methos

# print(d.keys())
# print(d.values())
# print(d.items())
# update={"update":"herrish"}
# d.update(update)
# print(d)

# print(d.get("Mihir"))#same as d['mihir] but not throw anyh error

#..........set.............



# s = {1,2,3,4,5,1,2,3,4,5}
# print(s)#non repetation

# #methods.....................

# s.add(6)
# s.add(7)
# print(s)
# print(len(s))
# s.remove(7)
# print(s)

#1

# d = {'kemcho': 'how are you',
#      'pankho' : 'fan'}
# print(d.keys())
# a  = input("enter th jugjuu word : ")
# print(d.get(a))

#2....

# s1 = int(input("Enter number : "))
# s2 = int(input("Enter number : "))
# s3 = int(input("Enter number : "))
# s4 = int(input("Enter number : "))
# s5 = int(input("Enter number : "))

# s = {s1,s2,s3,s4,s5}
# print(s)

#3.....

# s = {3,"3",3.3}
# print(s)

#4

# s = set()
# s.add(20)
# s.add("20")
# s.add(20.20)
# print(len(s))

#5...
# s = {}
# print(type(s))

#6...

# d = {}
# f1 = input("Enter a language mihir : ")
# f2 = input("Enter a language spike : ")
# f3 = input("Enter a language  destro: ")

# d ['mihir'] = f1
# d ['spike'] = f2
# d ['destro'] = f3

# print(d)

#7........
s= {1,2,[1,2]}#list is unhashable so in set only hashable are allowed like "..TUPLE.." 
print(s)


