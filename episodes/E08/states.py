# Three Pharos Cloud jobs through their states: round robin, 4 ms time slice
import csv
from collections import deque

jobs = list(csv.DictReader(open("processes.csv")))[:3]
need = {"ABC"[k]: int(j["burst_ms"]) for k, j in enumerate(jobs)}
SLICE, DISK = 4, {"C": (1, 3)}    # C: 1 ms of CPU, then 3 ms on the disk
ready, waiting, ran = deque(need), {}, dict.fromkeys(need, 0)
wait, cpu, log = dict.fromkeys(need, 0), [], []
run, used, t = None, 0, 0
while any(ran[p] < need[p] for p in need):
    for p in [p for p in waiting if waiting[p] == t]:
        del waiting[p]; ready.append(p); log.append((t, p, "waiting -> ready"))
    if run is None and ready:
        run, used = ready.popleft(), 0; log.append((t, run, "ready -> running"))
    for p in ready: wait[p] += 1          # 1 ms spent in the ready queue
    cpu.append(run); t += 1
    if run is None: continue
    ran[run] += 1; used += 1
    if ran[run] == need[run]: log.append((t, run, "running -> terminated")); run = None
    elif DISK.get(run, (0,))[0] == ran[run]:
        waiting[run] = t + DISK.pop(run)[1]; log.append((t, run, "running -> waiting")); run = None
    elif used == SLICE:
        ready.append(run); log.append((t, run, "running -> ready")); run = None

for when, p, change in log: print(f"t={when:>2}  {p}  {change}")
bars = [[cpu[0], 0, 1]]
for k, p in enumerate(cpu[1:], 1):
    if p == bars[-1][0]: bars[-1][2] = k + 1
    else: bars.append([p, k, k + 1])
print("CPU timeline   :", "  ".join(f"{p} {a}-{b}" for p, a, b in bars))
print("context switches:", len(bars) - 1)
print("ready waits (ms):", ", ".join(f"{p} {wait[p]}" for p in need))
with open("states_gantt.txt", "w") as f:
    f.write("Round robin, 4 ms slice, C waits 3 ms for the disk\n")
    f.write("  gantt  : " + "  ".join(f"{p} {a}-{b}" for p, a, b in bars) + "\n")
    f.write("  waits  : " + ", ".join(f"{p} {wait[p]}" for p in need) + "\n")
    f.write(f"  average: {sum(wait.values()) / len(need):.2f} ms\n")
