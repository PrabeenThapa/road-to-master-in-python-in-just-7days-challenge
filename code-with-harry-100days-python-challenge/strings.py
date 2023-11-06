#anything enclose between single or double quotation is string
name="Prabin"
print("MY name is "+ name)

# triple single or double quote is used for multiline string

conv = '''hello,
its me prabin
he said to me,"I am gooD"'''
print(conv)

#indexing
print(name[0],name[2])# it gives P a but if i want to get Pa then we must store in new string

Pa=name[0]+name[2]
print(Pa)

#Looping through a string
"""We can loop through strings using a for loop """
for character in name:
    print(character)
