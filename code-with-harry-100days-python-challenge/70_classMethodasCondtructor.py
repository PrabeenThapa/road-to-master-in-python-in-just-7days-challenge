class Employee:
    def __init__(self, n,s) -> None:
        self.name = n
        self.salary= s

    @classmethod#as alternztive constructor
    def fromStr(cls, string):
        return Employee(string.split("-")[0],string.split("-")[1])


e1 = Employee("Harry", 23323)
print(e1.name)
print(e1.salary)

string = "hello-world"
# e2=Employee(string.split("-")[0],string.split("-")[1])
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

#Alternative example

class Person:
    def __init__(self,n, a):
        self.name = n
        self.age=a

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))


person = Person.from_string("hello world, 20")
print(person.name, person.age)