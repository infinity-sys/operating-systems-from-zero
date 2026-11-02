# Create and finish 1,000 threads, then 1,000 processes, and compare
import os, time, threading
N = 1000
t = time.perf_counter()
for _ in range(N):
    th = threading.Thread(target=lambda: None); th.start(); th.join()
thread_ms = (time.perf_counter() - t) / N * 1000
t = time.perf_counter()
for _ in range(N):
    if os.fork() == 0: os._exit(0)
    os.wait()
fork_ms = (time.perf_counter() - t) / N * 1000
print(f"thread start + join : {thread_ms:.3f} ms each")
print(f"fork + wait         : {fork_ms:.3f} ms each")
print(f"a thread is about {fork_ms / thread_ms:.0f} times cheaper")
