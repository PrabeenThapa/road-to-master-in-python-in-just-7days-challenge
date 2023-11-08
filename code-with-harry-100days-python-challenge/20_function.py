#program to print gmean
def gmean(a,b):
    mean = (a+b)/(a*b)
    print(mean)

a1=2
a2=3
gmean(a1,a2)

b1=5
b2=4
gmean(b1,b2)

#comparator program
def isGreater(a,b):
    if(a>b):
     print(a,"is greater than ",b)
    else:
     print("a is less than b")
    
c1=4
c2=8
isGreater(c2,c1)

def isLesser(a,b):
   pass
#function types: a. Built-in functions, b.User-defined function