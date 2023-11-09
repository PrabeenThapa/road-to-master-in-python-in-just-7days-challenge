a = int(input("Enter any value between 5 and 10: "))
if (a<5 or a>10):
    raise ValueError("Value should be between 5 and 10.")
else:
     print(f"Enetred value is {a}")

print("If error this line won't be executed")