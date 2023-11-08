def average(a=2,b=4):#function with default arguement
    print("The average is ",(a+b)/2)
average(4,5)
average()
average(3)# is same as average(a=3)
average(b=9)

average(b=3,a=9)#if we give the arguement like this order doesnot matter

#variable length arguement

def average1(*numbers):#here numbers is of type tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is ", sum/len(numbers))

average1(5,4,2,3,1)

#keyword arbitrary arguement
#The function accesses the arguements by processing them in the formof dictionary

def name(**name):#here name of dict type
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname="singh", fname="Kehar",lname="Thapa")

#use of return statement

def sum1(*num):
    sum2=0
    for i in num:
        sum2=sum2+i
    return sum2

result = sum1(2,3,4)
print("The sum is ", result)