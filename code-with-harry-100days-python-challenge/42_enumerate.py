#without enumeration

marks = [12,23,34,34]
ind=0
for mark in marks:
    print(mark)
    if ind==2:
        print("Index 2")
        break
    ind+=1

#with enumeration

for index, mark in enumerate(marks):
    print(mark)
    if(index == 2):
        print("index 2")
        break

#start index
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 2):
        print("index 2")
        break