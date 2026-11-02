# On Linux every thread is a task: list /proc/self/task while 4 workers are alive
import os, threading
stop = threading.Event()
workers = [threading.Thread(target=stop.wait) for _ in range(4)]
for w in workers: w.start()
tasks = sorted(map(int, os.listdir("/proc/self/task")))
print(f"PID           : {os.getpid()}")
print(f"tasks         : {len(tasks)} (main + {len(workers)} workers)")
print(f"task ids      : {tasks[0]} ... {tasks[-1]}")
print(f"Threads line  : {[l for l in open('/proc/self/status') if l.startswith('Threads')][0].split()[1]}")
stop.set()
for w in workers: w.join()
print(f"after join    : {len(os.listdir('/proc/self/task'))} task")
