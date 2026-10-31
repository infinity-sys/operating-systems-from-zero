# Copy a file in 4096-byte pieces, counting calls.
import os

with open("data.bin", "wb") as f:
    f.write(b"x" * 10_000)              # 10,000 bytes

src = os.open("data.bin", os.O_RDONLY)
flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
dst = os.open("copy.bin", flags, 0o644)
reads = writes = 0
while True:
    chunk = os.read(src, 4096)
    reads += 1
    if not chunk:                        # 0 bytes: the end
        break
    print("read", len(chunk), "bytes")
    os.write(dst, chunk)
    writes += 1
os.close(src)
os.close(dst)
print("reads:", reads, "writes:", writes)
