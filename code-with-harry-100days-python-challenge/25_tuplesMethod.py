#directly manipulation of tuples cannot be done so we do convert tuple into list and then after operation it's converted into tuples
country=("Nepal", "USA", "UK")
temp = list(country)
temp.append("India")
temp.pop(1) #to remove member 
temp[2]= "Japan"
country = tuple(temp)
print(country)

nationality = ("Nepalese", "British", "Japanese")

con = country + nationality
print(con)

# pos = country.count("Japan") #It'll raise the error if there is no such member
pos = country.index("Japan")
print("Position of Japan in tuple is: ", pos)

num = ( 3, 4, 1, 5, 3,  9, 2, 3)
res = num.index(3, 1, 6)
print("Position of 3 in between pos 1 to pos 6 is: ",res)

