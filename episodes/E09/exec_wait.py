# fork + exec + wait: the child becomes another program; the parent collects its status
import os
pid = os.fork()
if pid == 0:
    os.execvp("uname", ["uname", "-s", "-r"])   # replaces the child's program
    print("never printed: exec does not return")
_, status = os.waitpid(pid, 0)
print(f"parent: child {pid} ran uname, exit code {os.waitstatus_to_exitcode(status)}")
pid = os.fork()
if pid == 0:
    os._exit(3)                      # a child that fails with code 3
_, status = os.waitpid(pid, 0)
print(f"parent: child {pid} exited with code {os.waitstatus_to_exitcode(status)}")
