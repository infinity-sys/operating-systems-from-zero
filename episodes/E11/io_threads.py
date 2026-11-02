# 8 Pharos jobs each wait 200 ms for the network: one by one, then with 8 threads
import time, threading
def fetch(): time.sleep(0.2)          # a stand-in for waiting on the network
t = time.perf_counter()
for _ in range(8): fetch()
one_by_one = time.perf_counter() - t
t = time.perf_counter()
ths = [threading.Thread(target=fetch) for _ in range(8)]
for th in ths: th.start()
for th in ths: th.join()
threads = time.perf_counter() - t
print(f"one by one : {one_by_one:.3f} s")
print(f"8 threads  : {threads:.3f} s")
print(f"speed-up   : {one_by_one / threads:.1f} times")
