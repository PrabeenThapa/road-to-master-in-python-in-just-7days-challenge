#Just trying
questions = ["Who the fuck is primeminister of Nepal?", "The capital city of Nepal is: ", "Two zero two four: "]
answer = ["Prachandey", "KTM", 2024]
cash = 1000
choices = [["KP", "Prachandey", "Mahendra", "Balen"],["KTM", "PLP", "BTL", "LALITPUR"], ["0044", "2024", "0024", "2044"]]


print("Lets start the game. Best of luck!")

for i in range (0,3):
    print(questions[i])
    print(choices[i])
    usrAns= input("Enter choices: ")

    match usrAns:
        case 'A':
            j=0
        case 'B':
            j=1
        case 'C':
            j=2
        case 'D':
            j=3

    if(choices[i][j]==answer[i]):
        print("You are correct.")
        cash = cash + 2 * cash
    else:
        print("Sorry!")

print("You've earned Rs.", cash, "\nCongratulations!")
