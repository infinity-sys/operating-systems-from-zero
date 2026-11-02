# Push 256 MB through a pipe, 64 KB per write, and time it
import os, time
SIZE, CHUNK = 256 * 1024 * 1024, 64 * 1024
block = b"x" * CHUNK
r, w = os.pipe()
t = time.perf_counter()
if os.fork() == 0:                    # child: the writer
    os.close(r)
    for _ in range(SIZE // CHUNK): os.write(w, block)
    os._exit(0)
os.close(w); got = reads = 0          # parent: the reader
while n := len(os.read(r, CHUNK)): got += n; reads += 1
os.wait(); took = time.perf_counter() - t
print(f"writes        : {SIZE // CHUNK:,} of {CHUNK:,} bytes")
print(f"reads         : {reads:,}")
print(f"bytes moved   : {got:,}")
print(f"time          : {took:.3f} s = {got / 2**20 / took:,.0f} MB/s")
