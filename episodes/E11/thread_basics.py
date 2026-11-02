# Threads share the process's memory: a change by one thread is seen by all
import os, threading
x = 10
def worker():
    global x
    x += 1                            # the same x as the main thread's
    print(f"thread: PID {os.getpid()}, thread id {threading.get_native_id()}, x = {x}")
t = threading.Thread(target=worker)
t.start(); t.join()
print(f"main  : PID {os.getpid()}, thread id {threading.get_native_id()}, x = {x}")
