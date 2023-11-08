#tuples are immutable
tup1=(2)
tup2=(2,)#single valued tuple
print(type(tup1))
print(type(tup2))
tup = (1, 2, 4, 6, "hello", True)

print(type(tup))
print(tup[1])#indexing is same as list
if True in tup:
    print("yes")

#slicing of tuple is same as the slicing of list but original tuple cannot be stored so it must be stored in another tuple variable
tup3=tup[1:-1]
print(tup3)
