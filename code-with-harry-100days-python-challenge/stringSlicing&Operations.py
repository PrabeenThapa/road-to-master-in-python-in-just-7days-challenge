name= "prabin, peakie, pynt"
print(name[0:10])#include 0 but not 10
print(name[:10])
print(name[1:10])
# print[4:] It'll throw an error
len1= len(name)
print(len1 , "is length of name string")

# negative slicing of string
print(name[1:-4])
print(name[1: len(name)-4])
print(name[-3:-1])
print(name[len(name)-3:len(name)-1])

#Loop through string
''''Strings are arrays and arrays are always iterable'''

Alpha= "ABCDEFGHI"
for i in Alpha:
    print(i)