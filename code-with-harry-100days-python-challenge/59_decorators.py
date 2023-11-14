# A decorator is a function that takes aother function as an aruguemet and returns a ne function that modifies the behaviour of original function.

def greet(fx):
    def mfx():
        print("Good morning.")
        fx()
        print("Thanks")
    return mfx

@greet
def hello():
    print("Hello world.")

# @greet #will throw error since there's no local variable to accept it
def add(a,b):
    return a+b

hello()
s = add(3,4)
print(s)