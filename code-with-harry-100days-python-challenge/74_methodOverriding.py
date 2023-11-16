#method overloading and method overriding
#polymorphism

#method overloading # python doesnot support method overloading directly

class student:
    def __init__(self, n1, n2):
        self.m1 = n1
        self.m2 = n2

    def sum(self, a=None, b=None, c= None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a + b

        else:
            s = a

        return s
    
s1 = student(3,4)
print(s1.sum(20,10,20))

#method overriding

class A:
    def show(self):
        print("In A show.")
class B(A):
    def show(self):
        print("In B show.")

a1 = A()
a1.show()
b1 = B()
b1.show()