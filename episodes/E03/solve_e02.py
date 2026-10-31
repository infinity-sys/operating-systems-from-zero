# Solution of the E02 exercise.
# Timer every 10 ms, job needs 35 ms of CPU,
# each interrupt costs 0.1 ms of OS work.
period, job, cost = 10, 35, 0.1

# ticks while the job is still running
ticks = list(range(period, job, period))
os_work = len(ticks) * cost
finish = job + os_work
ms = ", ".join(f"{t} ms" for t in ticks)
print("ticks at   :", ms)
print("interrupts :", len(ticks))
print("OS work    :", round(os_work, 2), "ms")
print("job ends at:", round(finish, 2), "ms")
print("overhead   :", f"{os_work / finish:.2%}")
