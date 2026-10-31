# Three jobs reach the CPU of pharos-01 at the same moment (time 0).
jobs = [("backup", 24), ("web-1", 3), ("web-2", 3)]   # (name, CPU burst in ms)

def run(order):
    """Run the jobs one after another; return the Gantt chart and each job's wait."""
    t, gantt, wait = 0, [], {}
    for name, burst in order:
        wait[name] = t                 # time spent waiting before it first runs
        gantt.append((name, t, t + burst))
        t += burst
    return gantt, wait

plans = [("arrival order", jobs),
         ("shortest first", sorted(jobs, key=lambda j: j[1]))]
for label, order in plans:
    gantt, wait = run(order)
    avg = sum(wait.values()) / len(wait)
    print(label)
    print("  gantt  :", "  ".join(f"{n} {a}-{b}" for n, a, b in gantt))
    print("  waits  :", ", ".join(f"{n} {w}" for n, w in wait.items()))
    print("  average:", avg, "ms")
