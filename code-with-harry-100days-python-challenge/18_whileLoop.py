#while loop
i=0
while(i<=10):
    print(i)
    i=i+1
i=1
a=int(input("Enter number of iteration: "))
while(i<=a):
    b=int(input("Input: "))
    print(b)
    i=i+1

count = 5
while(count>0):
    print(count)
    count=count -1
else:
    print("Inside else")
#do_while loop equivalent in python: 
count = 1
while True:
    print("This will be executed at least once.")
    count = count+ 1
    if count > 5:
        break


