import time
timeStamp = time.strftime("%H:%M:%S")
print(timeStamp)

#Exercise start
hour = int(time.strftime("%H"))
if (hour>12):
    print("Good afternoon!.")
elif (hour<12):
    print("Good morning!.")
else:
    print("Error has occured.")