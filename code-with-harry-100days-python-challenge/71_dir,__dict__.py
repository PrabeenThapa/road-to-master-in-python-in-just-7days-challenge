x = (1, 2, 3)
print(dir(x))
print(x.__add__)


#the __dict__ attribute
#it returns a dictionary representation of an object's attribute

class person:
    def __init__(self,n ,a):
        self.name= n
        self.age=a

p = person("prab", 20)
print(p.__dict__)#return all the attribute

#help() method
#it's used to get help documentaton for an object

print(help(str))
print(help(person))