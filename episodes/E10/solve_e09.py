# E09 exercise: os.fork(); if os.fork() == 0: os.fork(); print("hi")
import os
top = os.getpid()
r, w = os.pipe()
if os.fork() == 0:                    # a fresh "original" process P
    P = os.getpid(); os.close(r)
    os.fork()
    if os.fork() == 0:
        os.fork()
    os.write(w, f"{os.getpid()} {os.getppid()} {P}\n".encode())   # one "hi"
    os.close(w)
    while True:                       # stay alive until all children are gone
        try: os.wait()
        except ChildProcessError: break
    os._exit(0)
os.close(w); os.wait()
data = b""
while chunk := os.read(r, 4096): data += chunk
rows = [tuple(map(int, ln.split())) for ln in data.decode().split("\n") if ln]
P = rows[0][2]
print("hi printed               :", len(rows), "times")
print("processes                :", len(rows), f"(the original + {len(rows) - 1} new)")
print("children of the original :", sum(1 for pid, ppid, _ in rows if ppid == P))
print("processes that forked    :", len({ppid for _, ppid, _ in rows if ppid != top and ppid in {p for p, _, _ in rows}}))
