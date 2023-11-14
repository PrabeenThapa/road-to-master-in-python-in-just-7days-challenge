def greet(fx):
    def mfx(*arg, **kwargs):
        print("Good morning")
        fx(*arg, **kwargs)
        print("Thanks")
    return mfx

@greet
def hello():
    print("Hello world")
    
@greet
def add(a,b):
    print("result:",a+b)

hello()
add(2,3)