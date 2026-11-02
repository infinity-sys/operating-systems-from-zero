# E08 exercise: B sshd 3 ms, C logrotate 2 ms (1 ms, disk 2 ms, 1 ms), slice 2 ms
import csv
from collections import deque

jobs = list(csv.DictReader(open("processes.csv")))[1:3]
need = {"BC"[k]: int(j["burst_ms"]) for k, j in enumerate(jobs)}
SLICE, DISK = 2, {"C": (1, 2)}     # C: 1 ms of CPU, then 2 ms on the disk
ready, waiting, ran = deque(need), {}, dict.fromkeys(need, 0)
wait, cpu, state, disp = dict.fromkeys(need, 0), [], {}, 0
run, used, t = None, 0, 0
while any(ran[p] < need[p] for p in need):
    for p in [p for p in waiting if waiting[p] == t]:
        del waiting[p]; ready.append(p)
    if run is None and ready:
        run, used = ready.popleft(), 0; disp += 1
    for p in ready: wait[p] += 1
    state[t] = {p: "running" if p == run else "ready" if p in ready else
                "waiting" if p in waiting else "terminated" for p in need}
    cpu.append(run or "idle"); t += 1
    if run is None: continue
    ran[run] += 1; used += 1
    if ran[run] == need[run]: run = None
    elif DISK.get(run, (0,))[0] == ran[run]:
        waiting[run] = t + DISK.pop(run)[1]; run = None
    elif used == SLICE:
        ready.append(run); run = None

bars = [[cpu[0], 0, 1]]
for k, p in enumerate(cpu[1:], 1):
    if p == bars[-1][0]: bars[-1][2] = k + 1
    else: bars.append([p, k, k + 1])
print("CPU timeline :", "  ".join(f"{p} {a}-{b}" for p, a, b in bars))
print("dispatches   :", disp)
print("at t = 4.5   :", ", ".join(f"{p} {s}" for p, s in state[4].items()))
print("ready waits  :", ", ".join(f"{p} {wait[p]} ms" for p in need))
