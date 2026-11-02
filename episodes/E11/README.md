# E11 — Threads: Many Workers in One Process

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs):

- `solve_e10.py` — solution of the E10 exercise: tries all 70 orders of
  P's and Q's 8 read/write steps and counts the final values (largest 4,
  smallest 2).
- `thread_basics.py` — the E09 fork experiment with a thread: the worker
  adds 1 to the global `x` and the main thread sees it (x = 11 for both,
  same PID, two thread IDs).
- `thread_tasks.py` — starts 4 waiting threads and lists
  `/proc/self/task` (Linux only): 5 tasks, then 1 after join.
- `create_cost.py` — 1,000 threads (start + join) against 1,000 processes
  (fork + wait), time per item (Linux or macOS).
- `io_threads.py` — 8 jobs that each sleep 200 ms, one by one and then with
  8 threads, and the speed-up.

Run them inside the `~/pharos` folder from E05:

```bash
python3 solve_e10.py
python3 thread_basics.py
python3 thread_tasks.py
python3 create_cost.py
python3 io_threads.py
```

Times change on every run.
