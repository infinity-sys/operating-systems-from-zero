# A real timer "interrupt" from Python: the OS taps our program every 10 ms.
# (signal.setitimer works on Linux and macOS; on Windows, run it in WSL2.)
import signal, time

ticks = []
start = time.perf_counter()

def on_tick(signum, frame):              # the handler: runs when the tap arrives
    ticks.append((time.perf_counter() - start) * 1000)

signal.signal(signal.SIGALRM, on_tick)
signal.setitimer(signal.ITIMER_REAL, 0.010, 0.010)   # every 10 ms

x = 0
while time.perf_counter() - start < 0.105:   # a busy job: 105 ms of counting
    x += 1
signal.setitimer(signal.ITIMER_REAL, 0)      # stop the timer

print("the job counted to", f"{x:,}")
print("timer taps         :", len(ticks))
print("first three at (ms):", ", ".join(f"{t:.1f}" for t in ticks[:3]))
print("last one at (ms)   :", f"{ticks[-1]:.1f}")
