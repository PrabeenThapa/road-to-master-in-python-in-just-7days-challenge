#operator overloading

class vector:
    def __init__(self, i , j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return vector(self.i+ x.i, self.j+x.j, self.k+x.k)

v1 = vector(2, 4 ,5)
print(v1)

v2 = vector(1, 5, 6)
print(v2)

print(v1 + v2)
print(type(v1+v2))