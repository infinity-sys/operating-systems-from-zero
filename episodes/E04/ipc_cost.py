# Function call vs. message to another process.
# Microkernel services talk by messages.
import os, time

N = 20_000

def service(x):              # a "service" as a function
    return x + 1

t0 = time.perf_counter()
for i in range(N):
    service(i)
t1 = time.perf_counter()

# The same service in another process, via pipes
r1, w1 = os.pipe()           # requests
r2, w2 = os.pipe()           # replies
if os.fork() == 0:           # child: the server
    for i in range(N):
        os.write(w2, os.read(r1, 1))
    os._exit(0)

t2 = time.perf_counter()
for i in range(N):
    os.write(w1, b"x")       # send a request
    os.read(r2, 1)           # wait for the reply
t3 = time.perf_counter()
os.wait()

f_us = (t1 - t0) / N * 1e6
m_us = (t3 - t2) / N * 1e6
print(f"function call : {f_us:8.3f} µs each")
print(f"message (IPC) : {m_us:8.3f} µs each")
print(f"message is about {m_us / f_us:,.0f} times slower")
