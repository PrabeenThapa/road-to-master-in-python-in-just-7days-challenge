# Greeting 
import time
t = time.strftime("%H:%M:S")
hour =int(time.strftime("%H"))
print(hour)

if(hour>=0 and hour<12):
    print("Good morning")
elif(hour>=12 and hour<17):
    print("Good afternoon")
elif(hour>=17):
    print("Good night")