#Sets are collection of unordered data item 
#Sets are unchangeable and cannot store duplicate item in set

s = {2,8,6,2,"Hello"}
print(s)
# print(s[0])# member of set cannot be accessed by index

name = {}#it's empty dict not empty set 
name = set()#creating empty set
print(type(name))

#member can be accessed using for loop
for i in s:
   print(i)