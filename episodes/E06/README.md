# E06 — System Calls from Python: Talking to the Kernel

Video: VIDEO_LINK_PLACEHOLDER

Files in this folder (standard library only, no installs):

- `solve_e05.py` — solution of the E05 exercise: `-rwxr-x---` is 750; group
  `ops` can run it, others cannot read it. It then sets 750 on `run.sh` with
  `os.chmod` and reads it back with `os.stat`.
- `fds.py` — opens `notes.txt` and `run.sh` with `os.open` and prints the file
  descriptors (3 and 4), closes 3 and reopens (3 again: lowest free number).
- `rw.py` — writes `Pharos backup ok\n` to `log.txt` with `os.write` (17 bytes),
  then reads it back with `os.read`: 6, 11, then 0 bytes (end of file).
- `info.py` — one `stat` call on `log.txt`: size, mode, inode, links, owner,
  last change.
- `copy.py` — copies a 10,000-byte file in 4,096-byte pieces and counts the
  calls: 4 reads (4096, 4096, 1808, 0) and 3 writes.

Run them inside the `~/pharos` folder from E05 (see the E05 README to create
it). `solve_e05.py` changes `run.sh` to 750; put it back with
`chmod 755 run.sh`. Inode numbers, owners and dates describe your machine.

Watch the system calls (Linux, `sudo apt install strace`):

```bash
strace -e trace=openat,read,write,close python3 rw.py
strace -e trace=read,write python3 copy.py
strace -c -f python3 -c pass
```

The video's output comes from Linux 6.12, Debian 13, Python 3.13, strace 6.13.
On screen, strace's long data strings are shortened to `xxx...` and the
`O_CLOEXEC` flag that Python adds is left out for width. `strace -c` counted
358 calls for `python3 -c pass` and 385 for `copy.py`.

```bash
python3 solve_e05.py && chmod 755 run.sh
python3 fds.py
python3 rw.py
python3 info.py
python3 copy.py
```

Requires: Python 3.10+. `os.open`, `os.read` and `os.write` also work on
macOS and Windows; `strace` is Linux only.

Your turn: a script copies 1,000,000 bytes with `os.read(src, 65536)` in a
loop. How many read calls (including the last one that returns 0), how many
write calls, and how many bytes does the last write send? Solved at the start
of E07.
