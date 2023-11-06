#It's like switch case

a= int(input("Enter the value: "))
match a:
    case 0:
        print("Input is 0.")
    case 5:
        print("Input is 5.")

    case _ if a!=10:
        print("a is not 10")

    case _:#used for invalid case
        print("Entered is ", a)