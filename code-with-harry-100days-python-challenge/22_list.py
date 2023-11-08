mar = [5,6,7,"Hello", True]
print(type(mar))
print(mar)
print(mar[0])
print(mar[2])

print(mar[-1])#negative indexing
print(mar[len(mar)-1])

mar[0]=12#item of list can be changed

print(mar)

if "Hello" in mar:#same thngs applied in string
    print("Yes")
else:
    print("No")

if "el" in "hello":
    print("Present")

print(mar[1:4])
print(mar[1:-1])
print(mar[1:4:2])#jump index
#It's same as string slicing

#List Comprehension
lst = [i*i for i in range(10) if i %2==0]
print(lst)
