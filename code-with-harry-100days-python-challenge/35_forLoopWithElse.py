#else can be used with for and while too

for i in range(3):
    print(i)
else:
    print("No i")


for i in range(5):
    print(i)
    if(i==3):
        break
else:
    print("No i")

#else with while
i=0
while(i<7):
    print(i)
    i=i+1
    if(i==3):
        break
else:
    print("No i")