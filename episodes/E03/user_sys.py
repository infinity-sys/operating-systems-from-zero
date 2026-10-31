# Where does the time go:
# user mode or kernel mode?
import os, resource

def cpu_times():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime, r.ru_stime  # user, kernel

def measure(label, job):
    u0, s0 = cpu_times()
    job()
    u1, s1 = cpu_times()
    print(f"{label:<16} user {u1 - u0:5.2f} s",
          f"  kernel {s1 - s0:5.2f} s")

def compute():          # pure Python math
    total = 0
    for i in range(3_000_000):
        total += i * i

def syscalls():         # 300,000 tiny writes
    fd = os.open(os.devnull, os.O_WRONLY)
    for _ in range(300_000):
        os.write(fd, b"x")
    os.close(fd)

measure("compute loop", compute)
measure("300,000 writes", syscalls)
