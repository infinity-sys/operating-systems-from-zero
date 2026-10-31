# E02 — Inside the Computer: CPU, Memory, Devices and Interrupts

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs):

- `solve_e01.py` — solution of the E01 exercise: jobs A 5 ms, B 2 ms, C 8 ms
  in arrival order (average wait 4.0 ms) and shortest first (3.0 ms).
- `toy_cpu.py` — a tiny processor: fetch, decode, execute on
  `LOAD 5, ADD 2, ADD 8, HALT`, printing the PC and ACC after each step (ACC = 15).
- `dis_peek.py` — the instructions Python itself runs for `a + b + c`
  (instruction names differ slightly between Python versions).
- `mem_layers.py` — your machine's memory layers from the OS: L1 and L2 cache,
  cache line, memory and disk size (macOS `sysctl` or Linux `/sys`).
- `mem_speed.py` — 4 KB copied in memory against 4 KB written and synced to
  the disk, and how many times slower the disk is.
- `timer_hand.py` — the hand example: a timer every 4 ms, a 10 ms job,
  0.2 ms per interrupt: 2 interrupts, 3.85% overhead.
- `tick.py` — a real 10 ms timer signal tapping a 105 ms busy loop.
  Linux and macOS only; on Windows run it in WSL2.

Measured numbers (`mem_layers.py`, `mem_speed.py`, `tick.py`) describe your
machine and will differ from the video. The video's numbers come from a
MacBook (macOS 27, Apple M4, Python 3.10).

```bash
python3 solve_e01.py
python3 toy_cpu.py
python3 dis_peek.py
python3 mem_layers.py
python3 mem_speed.py
python3 timer_hand.py
python3 tick.py
```

Requires: Python 3.10+.

Your turn: a timer interrupts the CPU every 10 ms and a job needs 35 ms of
CPU. How many timer interrupts happen while it runs (counting from 0, not
counting the start)? If each costs 0.1 ms of OS work, what share of the time
is overhead? Solved at the start of E03.
