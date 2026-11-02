# What does creating a process cost? 1,000 x (fork + exit + wait), then 1,000 x exec too
import os, time
N = 1000
t = time.perf_counter()
for _ in range(N):
    if os.fork() == 0: os._exit(0)
    os.wait()
fork_ms = (time.perf_counter() - t) / N * 1000
t = time.perf_counter()
for _ in range(N):
    if os.fork() == 0: os.execv("/bin/true", ["true"])
    os.wait()
exec_ms = (time.perf_counter() - t) / N * 1000
print(f"fork + wait        : {fork_ms:.3f} ms per process")
print(f"fork + exec + wait : {exec_ms:.3f} ms per process")
