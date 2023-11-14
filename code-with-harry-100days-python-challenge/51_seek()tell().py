with open ("myfile.txt", 'r') as f:
    print(type(f))
    f.seek(10)#move to the 10th byte in the file
    
    data= f.read(5)#read the next 5 bytes
    print(data)
    print(f.tell())#it returns current position with in the file
    
with open('sample.txt', 'w') as f:
    f.write('Hello world')
    f.truncate(5)

with open('sample.txt','r') as f:
    print(f.read())