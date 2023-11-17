a = True
print(a:=False)

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers))>0:
    print(numbers.pop())

#primitive way example

# foods = list()
# while True:
#     food = input("Enter food name: ")
#     if (food == "quit"):
#         break
    
#     foods.append(food)
# print(foods)

#using walrus operator
foods = list()
while (food:=input("Enter food name: "))!="quit":
    foods.append(food)
print(foods)