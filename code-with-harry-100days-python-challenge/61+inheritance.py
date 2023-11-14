class Employee:
    def __init__(self,name, ID):
        self.name = name
        self.ID = ID

    def showdetails(self):
        print(f"The name of employee: {self.name}\nThe name ID of employee: {self.ID}")

class Er(Employee):
    def salary(self):
        print("It's inside ER")



e = Employee("Rohan",200)
e.showdetails()
a = Er("PAR", 25)
a.showdetails()
a.salary()