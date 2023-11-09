try:
    l=[1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurd.")

finally:#it'll be executed even if error occured & return 0
    print("I'm always executed")

#demonstration with function 
def func():
    try:
        a=[2, 1, 6, 8]
        i = int(input("Enter index: "))
        print(a[i])
        return 1
    except:
        print("Error has occured.")
    
    finally:
        print("I'm always executed.")

x=func()
print(x)