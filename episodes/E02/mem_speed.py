# How big and how fast: memory (RAM) versus the disk, on this machine.
import os, shutil, time

GB, KB = 1024**3, 1024
ram = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
disk = shutil.disk_usage("/").total
print(f"memory (RAM)     : {ram / GB:.0f} GB")
print(f"disk             : {disk / GB:.0f} GB")

def sync(f):                       # make sure the bytes really reached the disk
    try:
        import fcntl
        fcntl.fcntl(f.fileno(), fcntl.F_FULLFSYNC)   # macOS: a full flush
    except (ImportError, AttributeError):
        os.fsync(f.fileno())                         # Linux / WSL2

block = os.urandom(4 * KB)         # one 4 KB block

n = 10_000
t = time.perf_counter()
for _ in range(n):
    copy = bytearray(block)        # copy the block inside memory
t_ram = (time.perf_counter() - t) / n

n = 100
t = time.perf_counter()
with open("speed_test.bin", "wb") as f:
    for _ in range(n):
        f.write(block)             # write the block to the disk ...
        sync(f)                    # ... and wait until it is stored
t_disk = (time.perf_counter() - t) / n
os.remove("speed_test.bin")

print(f"4 KB in memory   : {t_ram * 1e6:.2f} microseconds")
print(f"4 KB to the disk : {t_disk * 1e6:.0f} microseconds")
print(f"disk / memory    : about {t_disk / t_ram:,.0f} times slower")
