# Same program, run twice: two processes
import os
import sys

print("program :", os.path.basename(sys.argv[0]))
print("pid     :", os.getpid())
print("parent  :", os.getppid())
