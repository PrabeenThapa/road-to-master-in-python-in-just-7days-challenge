import random

def check(comp, user):
    if comp == user:
        return 0
    elif (comp==0 and user ==1):
        return -1
    
    elif (comp == 1 and user == 2):
        return-1
    elif (comp ==2 and user ==0):
        return -1
    else:
        return 1



comp = int(random.randint(0,2))
user = int(input("0 for Snake, 1 for water & 2 for Gun:"))

print("Computer choice: ", comp)
print("User choice: ", user)

score = check(comp,user)
if(score == 0):
    print("It's a draw.")
elif (score==-1):
    print("you lose.")
else:
    print("You win.")

