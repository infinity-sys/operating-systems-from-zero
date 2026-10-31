# The memory layers of this machine, asked from the OS (macOS sysctl or Linux /sys).
import os, platform, shutil, subprocess

def mac(key):
    return int(subprocess.run(["sysctl", "-n", key], capture_output=True, text=True).stdout)

def linux(index):
    size = open(f"/sys/devices/system/cpu/cpu0/cache/index{index}/size").read().strip()
    return int(size[:-1]) * 1024 if size.endswith("K") else int(size)

if platform.system() == "Darwin":
    l1, l2, line = mac("hw.l1dcachesize"), mac("hw.l2cachesize"), mac("hw.cachelinesize")
else:
    l1, l2 = linux(0), linux(2)
    line = int(open("/sys/devices/system/cpu/cpu0/cache/index0/coherency_line_size").read())

KB, GB = 1024, 1024**3
ram = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
disk = shutil.disk_usage("/").total
print(f"L1 cache   : {l1 // KB} KB")
print(f"L2 cache   : {l2 // KB // 1024} MB")
print(f"cache line : {line} bytes")
print(f"memory     : {ram // GB} GB")
print(f"disk       : {disk // GB} GB")
print(f"disk / L1  : {disk // l1:,} times bigger")
