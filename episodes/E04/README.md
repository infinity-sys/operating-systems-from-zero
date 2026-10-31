# E04 — Operating System Structures: Monolithic, Layered, Microkernel and Modules

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs):

- `solve_e03.py` — solution of the E03 exercise: open, read, write, close,
  exit: 5 system calls and 9 mode switches (exit never returns).
- `switches.py` — counts the mode switches and kernel entries of one request
  (read a block from a file) in a monolithic, a layered and a microkernel design.
- `ipc_cost.py` — times a plain function call against a message to another
  process and back through two pipes (`os.fork`, `os.pipe`).
- `kernel_info.py` — prints which kernel you are running and how many kernel
  modules (macOS: kernel extensions via `kmutil showloaded`) are loaded.

Linux, macOS and WSL2 (`os.fork` is not available on plain Windows).
Measured numbers (`ipc_cost.py`, `kernel_info.py`) describe your machine and
will differ from the video. The video's numbers come from a MacBook
(macOS 27, Apple M4, Python 3.10).

```bash
python3 solve_e03.py
python3 switches.py
python3 ipc_cost.py
python3 kernel_info.py
```

Requires: Python 3.10+.

Your turn: on a microkernel, an app prints a file: app → print server → file
server → disk driver, and every reply comes back the same way. Count the
messages, the kernel entries and the mode switches; then say what happens if
the disk driver crashes, on a microkernel and on a monolithic kernel. Solved at
the start of E05.
