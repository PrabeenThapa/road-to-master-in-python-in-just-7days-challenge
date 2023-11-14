# def double(x):
#     returnx*2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/2


print(double(5))
print(cube(3))
print(avg(2,3,4))

print(appl(cube, 2))

print(appl(lambda x: x*x, 2))

