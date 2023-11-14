#publically accesseable variable
class Employee:
    def __init__(self):
        self.name = "Hari"

a= Employee()
print(a.name)

#private
class Employee:
    def __init__(self):
        self.__name = "Hari"

a= Employee()
# print(a.__name)#double underscore prefixing so private variable cannot access by this
print(a._Employee__name)#can be accessed indirectly
print(a.__dir__())

#protected 
class Employee:
    def __init__(self):
        self._name = "Hari"

a= Employee()
print(a._name)