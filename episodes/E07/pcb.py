# A slice of this process's PCB, as Linux shows it
import os

WANT = ["Name", "State", "Pid", "PPid", "Uid",
        "Threads", "VmSize", "VmRSS",
        "voluntary_ctxt_switches"]
for ln in open("/proc/self/status"):
    key, _, val = ln.partition(":")
    if key in WANT:
        print(f"{key:24} {' '.join(val.split())}")

notes = os.open("notes.txt", os.O_RDONLY)
print("open files (fd)         ", sorted(
    int(x) for x in os.listdir("/proc/self/fd")))
os.close(notes)
