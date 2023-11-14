#READING a FILE
# f = open('myfile.txt', 'rt')
# # print(f)
# text = f.read()
# print(text)
# f.close()

f = open("myfile.txt", "wt")
f.write("Hello world")
f.close()

with open('myfile.txt', 'a') as f:#no need to close file
    f.write("Second code.")
