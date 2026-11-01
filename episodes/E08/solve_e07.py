# Solution of the E07 exercise: the heap of forecast.py on pharos-01
start, end = 0x55a4c2b1e000, 0x55a4c2d3f000
size = end - start
print(f"end - start : {hex(size)}")
print(f"in bytes    : {size:,}")
print(f"in KB       : {size // 1024:,}")
print(f"pages       : {size // 4096} of 4,096 bytes")
pcb = {"PID": True, "program counter": True, "open files": True, "list contents": False}
for field, inside in pcb.items():
    print(f"in the PCB? {field:15}: {'yes' if inside else 'no, in process memory'}")
