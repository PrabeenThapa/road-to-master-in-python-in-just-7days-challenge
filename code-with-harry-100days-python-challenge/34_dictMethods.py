#update()
empID1={122:45,123:56,124:75}
empID2={125:54, 126:67}
empID1.update(empID2)
print(empID1)

# empID1.clear()
print(empID1)
empt={}#empty dictionary
#pop method
empID1.pop(124)
print(empID1)
empID1.popitem()#will remove the last item
print(empID1)

# del empID1#it'll delete empID1 variable

del empID1[123]#it'll remove the 123 key and corresponding value
print(empID1)

