import os
print(os.getcwd())
f = open("t.txt")
s = f.read()
print(s)
f.close()