x = 4#global variable

def func1():
    global x
    # x=5#local variable
        # global x
    x = 6#it'll change it globally
    y=3
    print(f"local variable x:{x} & y:{y}")


func1()

# print(f"Value of y: {y}")#it'll throw an error
print(f"value of x: {x}")