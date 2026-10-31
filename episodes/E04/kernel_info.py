# Which kernel am I running, and how many
# modules (kernel extensions) are loaded?
import platform, subprocess

print("system :", platform.system())
print("release:", platform.release())
v = platform.version()
print("kernel :", v.split(";")[-1].strip()[:40])

if platform.system() == "Darwin":
    cmd = ["kmutil", "showloaded"]
    out = subprocess.run(cmd, capture_output=True,
                         text=True).stdout
    n = len(out.splitlines()) - 1        # minus header
    print("loaded kernel extensions:", n)
else:
    with open("/proc/modules") as f:
        print("loaded modules:", len(f.readlines()))
