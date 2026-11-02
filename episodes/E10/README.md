# E10 — Inter-Process Communication: Pipes and Shared Memory

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs; Linux or macOS,
because `os.fork` does not exist on Windows):

- `solve_e09.py` — solution of the E09 exercise: runs `fork(); if fork() == 0:
  fork(); print('hi')` and every process reports its PID and parent PID
  through a pipe (hi printed 6 times, 6 processes, 2 children of the original).
- `pipe_basics.py` — `os.pipe()` then `os.fork()`: the parent writes a
  24-byte message, the child reads it until end of file.
- `pipe_capacity.py` — fills a non-blocking pipe 1 KB at a time to measure
  its capacity (65,536 bytes on Linux).
- `pipe_speed.py` — sends 256 MB through a pipe in 64 KB writes and times it.
- `shm_basics.py` — 64 bytes of `multiprocessing.shared_memory`: the child
  writes, the parent reads with no read call.
- `shm_counter.py` — two processes add 1 to a shared counter 100,000 times
  each, without and then with a lock, and count the lost updates.

Run them inside the `~/pharos` folder from E05:

```bash
python3 solve_e09.py
python3 pipe_basics.py
python3 pipe_capacity.py
python3 pipe_speed.py
python3 shm_basics.py
python3 shm_counter.py
```

Counts and times change on every run.
