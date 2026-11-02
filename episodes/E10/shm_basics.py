# Shared memory: the child writes into it, the parent reads the same bytes, no copy
import os
from multiprocessing import shared_memory
shm = shared_memory.SharedMemory(create=True, size=64)
pid = os.fork()
if pid == 0:
    msg = b"logrotate: 36 MB freed"
    shm.buf[:len(msg)] = msg          # an ordinary memory write
    os._exit(0)
os.waitpid(pid, 0)
print(f"name   : /dev/shm/{shm.name}, exists: {os.path.exists('/dev/shm/' + shm.name)}")
print(f"parent : {bytes(shm.buf[:22]).decode()!r}")
print(f"size   : {shm.size} bytes")
shm.close(); shm.unlink()
