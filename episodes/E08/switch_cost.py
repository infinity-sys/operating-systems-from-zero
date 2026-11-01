# Measure a context switch: two processes on ONE CPU pass a byte back and forth
import os, time
def switches():                     # times this process left the CPU
    s = dict(ln.split(":") for ln in open("/proc/self/status"))
    return int(s["voluntary_ctxt_switches"]) + int(s["nonvoluntary_ctxt_switches"])
N = 100_000
os.sched_setaffinity(0, {0})        # parent and child share CPU 0
a_r, a_w = os.pipe(); b_r, b_w = os.pipe()
if os.fork() == 0:                  # child: wait for a byte, send it back
    c0 = switches()
    for _ in range(N):
        os.read(a_r, 1); os.write(b_w, b"x")
    os.write(b_w, str(switches() - c0).encode()); os._exit(0)
p0, start = switches(), time.perf_counter()
for _ in range(N):                  # parent: send, then wait for the answer
    os.write(a_w, b"x"); os.read(b_r, 1)
took, p1 = time.perf_counter() - start, switches()
child = int(os.read(b_r, 32)); os.wait()
total = (p1 - p0) + child
print(f"round trips       : {N:,}")
print(f"parent left CPU   : {p1 - p0:,} times")
print(f"child left CPU    : {child:,} times")
print(f"total time        : {took:.3f} s")
print(f"per switch        : {took / total * 1e6:.2f} microseconds")
