f = open("myfile.txt", 'r')

i=0
while True:
    i+=1
    line = f.readline()

    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"number in {i}X1 is {m1}.")
    print(f"number in {i}X2 is {m2}.")
    print(f"number in {i}X3 is {m3}.")
    print(line)
f.close()

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()