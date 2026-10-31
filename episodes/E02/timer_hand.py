# By hand, checked: a timer interrupts the CPU every 4 ms; a job needs 10 ms of CPU.
period, job, cost = 4, 10, 0.2      # ms between ticks, CPU the job needs, OS work per tick

ticks = list(range(period, job, period))       # ticks while the job is still running
overhead = len(ticks) * cost
finish = job + overhead
print("ticks at   :", ", ".join(f"{t} ms" for t in ticks))
print("interrupts :", len(ticks))
print("OS work    :", round(overhead, 2), "ms")
print("job ends at:", round(finish, 2), "ms")
print("overhead   :", f"{overhead / finish:.2%}")
