class Employee:
    def __init__(self,n):
        self.name = n
    def __len__(self):
        i = 0
        for c in self.name:
            i=i+1
        return i

e = Employee("hello")
print(e.name)
print(len(e))#magic method

def __str__(self):
    return f"The name of the employee is {self.name}(str)."

def __repr__(self):
    return f"The name of the employee is {self.name}(repr)."

def __call__(self):
    print("It's inside call.")

