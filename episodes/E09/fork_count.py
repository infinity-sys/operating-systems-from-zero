# How many processes do n forks in a row create? Each one reports through a pipe.
import os
def count(n):
    r, w = os.pipe()
    if os.fork() == 0:              # a fresh starter process, so the count is clean
        os.close(r)
        for _ in range(n):
            os.fork()               # every process alive forks again
        os.write(w, b"x")           # each process writes one byte
        os._exit(0)
    os.close(w); os.wait()
    got = b""
    while chunk := os.read(r, 4096): got += chunk
    return len(got)
for n in (1, 2, 3, 4):
    print(f"{n} fork(s) in a row: {count(n):>2} processes  (2^{n} = {2 ** n})")
