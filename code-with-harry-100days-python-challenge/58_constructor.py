class person:
    
    def __init__(self, n, o):#defining a constructor
        print("Hey inside constructor.")
        self.name = n
        self.occ = o

    def info(self):
        print (f"{self.name} is a {self.occ}.")

a = person("prelon", "gamer")
b = person("Hello", "world")
a.info()
b.info()