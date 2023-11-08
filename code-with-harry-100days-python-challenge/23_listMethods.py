lst = [11,22,3,4,22,22]
print(lst)
lst.append(0)
print(lst)

lst.sort()#It sorts member of list in ascending order
lst.sort(reverse=True)#It sorts member of lst in descending order
lst.reverse()
print(lst)
print(lst.index(22))#Gives the index of first order
print(lst.count(22))

#copy in list
m = lst.copy()#Don't use m = lst since it is copied with reference
m[0]= 5
print(m)

#inserting member in index
lst.insert(2,232)
print(lst)

#extend in list
a = [100,400,200,900]
K = lst + a#it merge lst and a
lst.extend(a)
print(lst)
print(K)