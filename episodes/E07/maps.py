# Where does this process live in memory?
import os

def show(name, line):
    rng, perms = line.split()[:2]
    lo, hi = (int(x, 16) for x in rng.split("-"))
    kb = (hi - lo) // 1024
    print(f"{name:6} {rng}  {perms}  {kb:>6} KB")

lines = open("/proc/self/maps").read().splitlines()
exe = os.path.realpath("/proc/self/exe")
for ln in lines:
    if ln.endswith(exe) and " r-xp " in ln:
        show("text", ln)
for ln in lines:
    if ln.endswith("[heap]"):
        show("heap", ln)
for ln in lines:
    if ln.endswith("[stack]"):
        show("stack", ln)
