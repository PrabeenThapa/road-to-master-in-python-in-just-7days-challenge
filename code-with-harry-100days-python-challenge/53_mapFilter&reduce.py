#traditiona way

def cube(x):
    return x*x*x
l = [1, 2, 3, 4, 5, 6]
newl=[]

for item in l:
    newl.append(cube(item))

print(newl)

#using MAP:
newl1 = list(map(cube, l))
print(newl)

#FILTER
def filter_function(a):
    return a>2
newl2 = filter(filter_function, l)
print(list(newl2))

#reduce
from functools import reduce #reduce should be import
numbers = [1, 2, 3, 4, 5]

def mysum(x,y):
    return x+y

sum=reduce (mysum, numbers)
print(sum)