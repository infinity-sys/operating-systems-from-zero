# The same 100,000 bytes:
# one system call, or 100,000 of them?
import os, time

N = 100_000
data = b"x" * N
fd = os.open(os.devnull, os.O_WRONLY)

t0 = time.perf_counter()
for i in range(N):
    os.write(fd, data[i:i + 1])  # 1 byte
t1 = time.perf_counter()
os.write(fd, data)               # all at once
t2 = time.perf_counter()
os.close(fd)

many, one = t1 - t0, t2 - t1
print(f"{N:,} calls of 1 byte : {many*1000:8.2f} ms")
print(f"1 call of {N:,} bytes : {one*1000:8.3f} ms")
print(f"cost per call         : {many/N*1e6:8.2f} µs")
print(f"one call is about {many/one:,.0f} times faster")
