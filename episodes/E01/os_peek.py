# Ask the operating system about itself, from Python.
import os, platform, subprocess, sys

print("system   :", platform.system(), platform.release())
print("machine  :", platform.machine())
print("cpu cores:", os.cpu_count())
print("my pid   :", os.getpid())

ps = subprocess.run(["ps", "-A", "-o", "pid="], capture_output=True, text=True)
print("processes:", len(ps.stdout.split()))
print("python   :", sys.version.split()[0])
