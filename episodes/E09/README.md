# E09 — fork, exec and wait: How Processes Are Born

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs; Linux or macOS,
because `os.fork` does not exist on Windows):

- `solve_e08.py` — solution of the E08 exercise: B sshd 3 ms, C logrotate
  2 ms (1 ms, a 2 ms disk wait, 1 ms), round robin with a 2 ms slice. It
  prints the CPU timeline, the dispatches, the states at t = 4.5 and the
  ready-queue waits. Reads `processes.csv` from E05.
- `fork_basics.py` — one `os.fork()`: the child sees 0 and changes its copy
  of `x`; the parent sees the child's PID and its `x` is unchanged.
- `fork_count.py` — 1 to 4 forks in a row; every process writes one byte
  into a pipe and the parent counts them (2, 4, 8, 16 = 2 to the power n).
- `exec_wait.py` — a child that becomes `uname` with `os.execvp`, and a
  child that exits with code 3; the parent collects both with `os.waitpid`.
- `fork_cost.py` — creates 1,000 processes with fork + wait, then 1,000
  with fork + exec of `true` + wait, and prints the time per process.

Run them inside the `~/pharos` folder from E05:

```bash
python3 solve_e08.py
python3 fork_basics.py
python3 fork_count.py
python3 exec_wait.py
python3 fork_cost.py
```

Output in the video (Linux 6.12, Debian 13, Python 3.13): CPU timeline
B 0-2, C 2-3, B 3-4, idle 4-5, C 5-6; 4 dispatches; at t = 4.5 B terminated,
C waiting; ready waits B 1 ms, C 2 ms. fork_count.py: 2, 4, 8, 16 processes.
exec_wait.py: uname prints Linux 6.12.94+, exit code 0; second child exit
code 3. fork_cost.py: fork + wait 0.458 ms per process, fork + exec + wait
0.901 ms. PIDs and times change on every run.

Your turn: `os.fork()`, then `if os.fork() == 0: os.fork()`, then
`print('hi')`. How many times is hi printed? Solved in E10.
