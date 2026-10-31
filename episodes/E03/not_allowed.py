# Ask the kernel for things a normal
# program is not allowed to do.
import os

# allowed: it only asks a question
print("my pid       :", os.getpid())

# 1. Raise my own priority (admin only)
try:
    os.nice(-5)
    print("nice(-5)     : allowed")
except PermissionError as e:
    print("nice(-5)     : refused,", e.strerror)

# 2. Signal process 1, the first process
#    (signal 0 only checks; it is not mine)
try:
    os.kill(1, 0)
    print("kill(1)      : allowed")
except PermissionError as e:
    print("kill(1)      : refused,", e.strerror)
