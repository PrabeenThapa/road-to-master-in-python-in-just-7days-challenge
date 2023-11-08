dic = {
    "Name":"Prabin",
    "empID":108,
    
}
print(dic["empID"])#will throw an error if there is no such key
print(dic.get("age"))#will throw none

#dictionary is ordered

info = {
    "name":"Prabin",
    "age":19,
    "eligible": True
}
print(info)

print(info.keys())
for key in info:#accessing values
    # print(info[key])
    print(f"The {key} is {info[key]}")

print(info.values())

print(info.items())

for key, value in info.items():
    print(f"The {key} is {info[key]}")