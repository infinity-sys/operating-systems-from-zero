# Write, then read, with raw system calls.
import os

flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
fd = os.open("log.txt", flags, 0o644)
n = os.write(fd, b"Pharos backup ok\n")
print("write ->", n, "bytes")
os.close(fd)

fd = os.open("log.txt", os.O_RDONLY)
print("read 6   ->", os.read(fd, 6))
print("read 100 ->", os.read(fd, 100))
print("read 100 ->", os.read(fd, 100))   # end of file
os.close(fd)
