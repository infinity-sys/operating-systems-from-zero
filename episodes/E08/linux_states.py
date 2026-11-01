# Make processes in four Linux states, then read each state from /proc
import os, signal, time

def state(pid):
    return open(f"/proc/{pid}/stat").read().split(") ")[1][0]

def child(work):
    pid = os.fork()
    if pid == 0: work(); os._exit(0)
    return pid

sleeper = child(lambda: time.sleep(30))      # waits for a timer
spinner = child(lambda: [0 for _ in iter(int, 1)])   # never stops computing
stopped = child(lambda: time.sleep(30)); os.kill(stopped, signal.SIGSTOP)
zombie = child(lambda: None)                 # exits at once; nobody waits yet
time.sleep(0.5)
for name, pid in [("sleeper", sleeper), ("spinner", spinner),
                  ("stopped", stopped), ("zombie", zombie)]:
    print(f"{name:8} pid {pid}  state {state(pid)}")
for pid in (sleeper, spinner, stopped): os.kill(pid, signal.SIGKILL)
for _ in range(4): os.wait()                 # collect all four children
