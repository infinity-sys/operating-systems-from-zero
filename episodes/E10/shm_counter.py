# Two processes add 1 to the same shared counter 100,000 times each
import os
from multiprocessing import shared_memory, Lock
N = 100_000
def run(lock):
    shm = shared_memory.SharedMemory(create=True, size=8)
    shm.buf[:8] = (0).to_bytes(8, "little")
    def add():
        for _ in range(N):
            if lock: lock.acquire()
            x = int.from_bytes(shm.buf[:8], "little")      # read
            shm.buf[:8] = (x + 1).to_bytes(8, "little")    # add 1, write back
            if lock: lock.release()
    kids = []
    for _ in range(2):
        pid = os.fork()
        if pid == 0: add(); os._exit(0)
        kids.append(pid)
    for pid in kids: os.waitpid(pid, 0)
    total = int.from_bytes(shm.buf[:8], "little")
    shm.close(); shm.unlink()
    return total
for name, lock in (("no lock  ", None), ("with lock", Lock())):
    total = run(lock)
    print(f"{name}: expected {2 * N:,}, got {total:,}, lost {2 * N - total:,}")
