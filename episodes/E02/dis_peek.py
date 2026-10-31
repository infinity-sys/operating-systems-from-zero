# Python's own "machine": the instructions it really executes for one line of code.
import dis

def total(a, b, c):
    return a + b + c

dis.dis(total)
