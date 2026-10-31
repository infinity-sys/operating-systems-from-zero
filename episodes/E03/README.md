# E03 — Kernel Mode, User Mode and System Calls

Video: https://youtu.be/QITGNh8K8LU

Files in this folder (standard library only, no installs):

- `solve_e02.py` — solution of the E02 exercise: a timer every 10 ms, a 35 ms
  job, 0.1 ms per interrupt: 3 interrupts, the job ends at 35.3 ms, 0.85% overhead.
- `not_allowed.py` — asks the kernel for things a normal program may not do
  (`os.nice(-5)`, a signal to process 1) and prints the kernel's answer.
- `read_file.py` + `hello.txt` — the five-line program whose system calls we
  predict by hand, then trace with `strace` (Linux):
  `strace -e trace=openat,read,write,close,exit_group python3 read_file.py`
- `user_sys.py` — user time against kernel time for pure math and for
  300,000 one-byte writes (`resource.getrusage`).
- `syscall_cost.py` — 100,000 bytes written one byte per call against one
  call, with the cost per call.

Linux, macOS and WSL2 (`resource`, `os.nice` and `strace` are not available on
plain Windows). Measured numbers (`user_sys.py`, `syscall_cost.py`) describe
your machine and will differ from the video. The video's numbers come from a
MacBook (macOS 27, Apple M4, Python 3.10); the strace run is Linux 6.12,
Python 3.13.

```bash
python3 solve_e02.py
python3 not_allowed.py
python3 read_file.py
strace -e trace=openat,read,write,close,exit_group python3 read_file.py   # Linux
python3 user_sys.py
python3 syscall_cost.py
```

Requires: Python 3.10+.

Your turn: a Python script opens a file, reads it, prints a line and exits.
List, in order, the system calls you expect (open, read, write, close, exit)
and mark which happen in user mode and which switch to kernel mode. Solved at
the start of E04.
