#variables
a=1
b= True
c="Prabin"
d= None

print(b)

#datatypes
e=5
print(a+e)
print("The type of a is ", type(b))
print("The type of d is ", type(d))

#1. numeric data: int, float, complex
c1 = complex( 2,4)
c2 = complex(4,1)
c3=c1+c2
print(c3)
print(type(c3))

#2. Text data: str
#3. Sequenced data: list, tuple
list1 = [1, 2, 3.4, ["apple" , "banana"]]# list is mutable(changeable) but tuple is immutable(unchangeable)
print(list1)

tuple1 = ("prabin", 123, ("hello", "world"))
print(tuple1)

#4. Mapped data: dict
#dict:  a dictionary is an unordered collection of data containing a key:value pair.

d1 = {"name":"prabin", "age":20}
print(d1)