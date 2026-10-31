# E05 — First Look at Linux: the Shell, Files and Processes

Video: https://youtu.be/hKZQN3Vk6ro

Files in this folder (standard library only, no installs):

- `solve_e04.py` — solution of the E04 exercise: printing on a microkernel,
  6 messages, 6 kernel entries, 12 mode switches.
- `paths.py` — follows `cd pharos`, `cd ../..`, `cd /etc` and `cd ~` from
  `/home/box`, the way the shell does (absolute vs relative, `..`, `~`).
- `perms.py` — reads the permission bits of every file in the current folder,
  by hand (r=4, w=2, x=1) and from the kernel (`os.stat`), side by side.
- `procs.py` — prints its own PID and its parent's (from `/proc/PID/comm`),
  counts running processes in `/proc`, then forks a child.

`procs.py` needs Linux or WSL2 (it reads `/proc`). The other scripts run on
Linux, macOS and WSL2. Numbers such as PIDs and process counts describe your
machine and will differ from the video. The video's output comes from Linux
6.12, Debian 13, Python 3.13; `ps` and `procs.py` ran in a small fresh PID
namespace (`unshare -Urpf --mount-proc`), which is why bash is PID 1 there.

To recreate the video's folder:

```bash
mkdir -p ~/pharos && cd ~/pharos
printf 'pharos-01 notes\n' > notes.txt
printf '#!/bin/sh\necho "backup done"\n' > run.sh
chmod 644 notes.txt && chmod 755 run.sh
ls -l && ./run.sh
```

```bash
python3 solve_e04.py
python3 paths.py
python3 perms.py
python3 procs.py
```

Requires: Python 3.10+.

Your turn: on pharos-01, `ls -l` shows `-rwxr-x--- 1 omar ops run.sh`. Write
the permissions as three digits. Can a member of group `ops` run it? Can
anyone else read it? Solved at the start of E06.
