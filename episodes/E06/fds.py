# File descriptors: small numbers the kernel hands out.
import os

a = os.open("notes.txt", os.O_RDONLY)   # system call
b = os.open("run.sh", os.O_RDONLY)
print("notes.txt ->", a)
print("run.sh    ->", b)

os.close(a)                              # 3 is free again
c = os.open("notes.txt", os.O_RDONLY)
print("reopened  ->", c)

os.close(b)
os.close(c)
