# Open a file, read it, print a line, exit.
f = open("hello.txt")
data = f.read()
print(data.strip())
f.close()
