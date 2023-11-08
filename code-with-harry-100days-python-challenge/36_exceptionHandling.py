a = input("Enter any number: ")
print(f"Multiplication table of {a}:")

try:
    for i in  range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Error occured!")

print("Some line of code.")
print("End of program")

try:
    num = int(input("Enter an integer: "))
    a=[6,4]
    print(a[num])
except ValueError:
    print("Number is not i=an integer.")
except IndexError:
    print("Index error")