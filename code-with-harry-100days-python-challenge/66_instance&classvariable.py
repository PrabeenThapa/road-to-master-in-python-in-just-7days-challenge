class Employee:
    companyName="samsung"
    noOfEmployees=0
    def __init__(self,Name) -> None:
        self.name = Name
        self.raiseamount = 0.02
        Employee.noOfEmployees +=1    
    def showDetails(self):
        print(f"The name of the employee is {self.name}.\nThe raise amount is {self.raiseamount}\nThe company name is {self.companyName}.\nThe entry of employee is {self.noOfEmployees}")


emp1 = Employee("Hari")
Employee.companyName="Nokia"
# emp1.showDetails()
Employee.showDetails(emp1)
emp2= Employee("Karan")
emp2.raiseamount = 4
emp2.companyName="apple"
emp2.showDetails()


