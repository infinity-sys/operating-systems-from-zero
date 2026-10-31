# E07 — What Is a Process? Memory Layout and the PCB

Video: https://youtu.be/SWVCgdLo3Lk

Files in this folder (standard library only, no installs):

- `solve_e06.py` — solution of the E06 exercise: copies 1,000,000 bytes in
  65,536-byte pieces with `os.read` / `os.write` and counts the calls:
  15 full pieces, leftover 16,960; 17 reads, 16 writes, last write 16,960.
- `pids.py` — prints its own PID (`os.getpid`) and its parent's
  (`os.getppid`). Run it twice: two processes, two PIDs, same parent.
- `maps.py` — reads `/proc/self/maps` and prints the text, heap and stack
  regions of its own process, with their sizes in KB.
- `pcb.py` — prints a slice of its own process control block from
  `/proc/self/status` (Name, State, Pid, PPid, Uid, Threads, VmSize, VmRSS,
  voluntary context switches) and its open file descriptors.

Run them inside the `~/pharos` folder from E05 (`pcb.py` opens `notes.txt`).
`solve_e06.py` creates `big.bin` and `big_copy.bin`; delete them afterwards.

```bash
python3 solve_e06.py
python3 pids.py; python3 pids.py
python3 maps.py
python3 pcb.py
strace -e trace=read,write python3 solve_e06.py
```

The video's output comes from Linux 6.12, Debian 13, Python 3.13, strace 6.13.
PIDs and addresses describe that machine and change on every run: Linux
places the regions at random (address space layout randomization).

Requires: Python 3.10+. `pids.py` runs everywhere; `maps.py` and `pcb.py`
need Linux (`/proc`), for example WSL2 on Windows.

Your turn: on pharos-01, the memory map of `forecast.py` shows a heap from
`0x55a4c2b1e000` to `0x55a4c2d3f000`. How big is the heap in bytes and in KB?
Does the heap grow up or down, and the stack? Which of these are kept in the
PCB: the PID, the program counter, the list of open files, the contents of a
Python list? Solved at the start of E08.
