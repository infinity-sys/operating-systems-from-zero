# E08 — Process States and Context Switches, by Hand

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs):

- `solve_e07.py` — solution of the E07 exercise: the heap from
  `0x55a4c2b1e000` to `0x55a4c2d3f000` is 0x221000 = 2,232,320 bytes =
  2,180 KB = 545 pages of 4,096 bytes; plus the PCB question.
- `states.py` — simulates the first three Pharos Cloud jobs from
  `processes.csv` (A csv-import 14 ms, B sshd 3 ms, C logrotate 2 ms with a
  3 ms disk wait after its first 1 ms), round robin with a 4 ms slice, one
  millisecond at a time. It prints every state transition, the CPU timeline,
  the number of context switches and the ready-queue waits, and writes
  `states_gantt.txt`.
- `switch_cost.py` — pins itself and a child to CPU 0 and passes a byte back
  and forth through two pipes 100,000 times; reads the real switch counters
  from `/proc/self/status` and prints the time per context switch.
- `linux_states.py` — creates four children in the states S (sleeping),
  R (running), T (stopped) and Z (zombie) and reads each state letter from
  `/proc/PID/stat`.
- `ctxt.py` — a sleeper and two CPU hogs on one CPU; prints each one's
  voluntary and nonvoluntary context switches.

Run them inside the `~/pharos` folder from E05 (`states.py` reads
`processes.csv`).

```bash
python3 solve_e07.py
python3 states.py
python3 switch_cost.py
python3 linux_states.py
python3 ctxt.py
```

Output in the video (Linux 6.12, Debian 13, Python 3.13): CPU timeline
A 0-4, B 4-7, C 7-8, A 8-12, C 12-13, A 13-19; 5 context switches; waits
A 5, B 4, C 8 ms, average 5.67 ms. switch_cost.py: 100,000 + 100,000
switches, 0.261 s, 1.31 microseconds per switch. ctxt.py: sleeper 100
voluntary, 0 nonvoluntary; hogs 0 voluntary, 268 and 258 nonvoluntary.
Times, counts and PIDs change on every run and every machine; the
`states.py` simulation is always the same.

Requires: Python 3.10+. `solve_e07.py` and `states.py` run everywhere; the
other three need Linux (`/proc`, `os.sched_setaffinity`), for example WSL2
on Windows.

Your turn: B (sshd) needs 3 ms of CPU; C (logrotate) needs 2 ms, but after
its first 1 ms it waits 2 ms for the disk. Both arrive at time 0, B first;
the time slice is 2 ms. Draw the timeline: is the CPU ever idle, and when?
How many times is a process dispatched (ready to running)? At t = 4.5, what
state is each process in, and what is each one's ready-queue wait? Solved at
the start of E09.
