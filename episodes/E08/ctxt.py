# Voluntary or not? A sleeper and two CPU hogs that share CPU 0
import os, time
def counters():
    s = dict(ln.split(":") for ln in open("/proc/self/status"))
    return (int(s["voluntary_ctxt_switches"]),
            int(s["nonvoluntary_ctxt_switches"]))
def sleeper():
    for _ in range(100): time.sleep(0.01)   # gives the CPU away 100 times
def hog():
    end = time.time() + 2
    while time.time() < end: pass           # never gives it away
os.sched_setaffinity(0, {0})           # all three children share CPU 0
pipes = []
for name, work in [("sleeper", sleeper), ("hog 1", hog), ("hog 2", hog)]:
    r, w = os.pipe()
    if os.fork() == 0:
        work(); v, n = counters()
        os.write(w, f"{name:8} voluntary {v:4}   nonvoluntary {n:4}\n".encode())
        os._exit(0)
    os.close(w); pipes.append(r)
for r in pipes: print(os.read(r, 100).decode(), end="")
for _ in pipes: os.wait()
