# How many bytes fit in a pipe before the writer must wait?
import os
r, w = os.pipe()
os.set_blocking(w, False)             # fail instead of waiting when full
total = 0
try:
    while True: total += os.write(w, b"x" * 1024)
except BlockingIOError:
    pass
print(f"pipe capacity : {total:,} bytes = {total // 1024} KB = {total // 4096} pages")
