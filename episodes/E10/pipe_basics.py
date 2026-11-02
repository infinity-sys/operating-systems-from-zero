# A pipe: the parent writes bytes, the child reads them, through the kernel
import os
r, w = os.pipe()                      # two file descriptors: read end, write end
pid = os.fork()
if pid == 0:                          # child: read until the parent closes its end
    os.close(w)
    got = b""
    while chunk := os.read(r, 1024): got += chunk
    print(f"child : read {len(got)} bytes: {got.decode()!r}", flush=True)
    os._exit(0)
os.close(r)
msg = "job 1004 csv-import done".encode()
print(f"parent: writing {len(msg)} bytes", flush=True)
os.write(w, msg); os.close(w)         # closing = end of file for the reader
os.waitpid(pid, 0)
print(f"parent: read end fd {r}, write end fd {w}")
