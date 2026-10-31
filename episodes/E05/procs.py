# Who am I, who is my parent, and how many processes?
import os, sys

def name(pid):                  # the kernel's record
    with open(f"/proc/{pid}/comm") as f:
        return f.read().strip()

me, parent = os.getpid(), os.getppid()
print("me    :", me, name(me))
print("parent:", parent, name(parent))

pids = [d for d in os.listdir("/proc") if d.isdigit()]
print("processes running now:", len(pids))

sys.stdout.flush()                   # before the copy
child = os.fork()                    # one becomes two
if child == 0:
    print("child :", os.getpid(), "parent", os.getppid(),
          flush=True)
    os._exit(0)
os.wait()
