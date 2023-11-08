#Exampleof recursion
#factorial of 4= 4*3*2*1

# factorial = n * factorial(n-1)

def fact(n):
    if (n==0 or n==1):
        return True
    else:
        return n*fact(n-1)
    
print("Fact of 5: ",fact(5))

#calculation of fibonacci series: 0 1 1 2 3 5 8 13 .....
#f(n) = f(n-1)+f(n-2)
def fibo(n):
    if n <= 0:
        return "Incorrect input"

    elif n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibo(n - 1) + fibo(n - 2)

n = 10
print("Fibonacci series:")
for i in range(1, n+1):
    print(fibo(i))
