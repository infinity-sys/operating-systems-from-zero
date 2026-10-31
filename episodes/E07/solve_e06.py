# E06 exercise: copy 1,000,000 bytes, 65,536 at a time
import os

SIZE, PIECE = 1_000_000, 65_536
with open("big.bin", "wb") as f:
    f.write(b"x" * SIZE)

src = os.open("big.bin", os.O_RDONLY)
dst = os.open("big_copy.bin", os.O_WRONLY | os.O_CREAT
              | os.O_TRUNC, 0o644)
reads = writes = last = 0
while True:
    chunk = os.read(src, PIECE)
    reads += 1
    if not chunk:
        break
    last = os.write(dst, chunk)
    writes += 1
os.close(src)
os.close(dst)

print("full pieces:", SIZE // PIECE)
print("leftover   :", SIZE % PIECE)
print("reads      :", reads)
print("writes     :", writes)
print("last write :", last)
