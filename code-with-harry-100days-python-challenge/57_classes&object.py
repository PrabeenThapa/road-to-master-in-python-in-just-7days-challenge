class person:
    name = "hello"
    occupation = 'soft'
    salary = 30
    def info(self):#self keyword
        print(f"{self.name} is a {self.occupation}")

a1 = person()
a1.name= "Rabin"
print(a1.name, a1.occupation)
a1.info()