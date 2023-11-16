#time module 
import time

# def usingwhile():
#     i = 0
#     while i<20:
#         print(i)
#         i = i+1


# def usingfor():
#     for i in range (0,20):
#         print(i)

# init = time.time()
# usingfor()
# print(time.time()-init)
# usingwhile()
# print(time.time()-init)

print(4)
time.sleep(3)#time.sleep
print("This is printed after 3 sec")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
