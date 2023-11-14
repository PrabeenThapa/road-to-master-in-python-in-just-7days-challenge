class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company name is {self.company}.")

    @classmethod
    def changecompan(cls, newcompany):
        cls.company = newcompany
    

e1 = Employee()
e1.name= "Hari"
e1.show()
e1.changecompan("Tesla")
e1.show()
