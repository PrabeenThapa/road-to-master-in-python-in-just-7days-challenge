s1 = {1, 2, 5, 8, 2}
s2 = {3, 4, 7}
print(s1.union(s2))#union operation
s1.update(s2)#update s1
print(s1)

print(s1.intersection(s2))#intersecrtion operation 
s2.intersection_update(s2)#intersection_update
print(s2)

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))


s1 = {2, 3, 5, 6, 8, 9, 0}
s2 = {x for x in range(0,6)}

s3 = s1.difference(s2)#difference
s1.difference_update(s2)#difference_update
print(s1)
print(s3)

a1 ={2,3,1}
a1.add(4)#adding member in existed set
print(a1)
a2={2,3,4,5}
a1.update(a2)
print(a1)
#remove()/discard()
a1.remove(2)#cannot remove multiple item and if there is no such member it will raise an error
a1.discard(2)#same as remove but doesnot raise an error

print(a1)

#pop() method
item = a1.pop()
print(item)#it'll popout any random member

#del and clear keyword
#del a1#it'll delete set a1 and if we want to print it it'll throw an error

a1.clear
print(a1)#it'll clear the member of a1

print( 3 in a2)
