# fork() returns twice: 0 in the child, the child's PID in the parent
import os
x = 10
pid = os.fork()
if pid == 0:                        # the child: a copy of the parent
    x += 1
    print(f"child : fork returned {pid}, my PID {os.getpid()}, parent {os.getppid()}, x = {x}", flush=True)
    os._exit(0)
os.waitpid(pid, 0)                  # the parent waits for the child
print(f"parent: fork returned {pid}, my PID {os.getpid()}, x = {x}", flush=True)
