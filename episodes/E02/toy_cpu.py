# A toy CPU: fetch, decode, execute, one instruction at a time.
memory = ["LOAD 5", "ADD 2", "ADD 8", "HALT"]   # the program sits in memory
pc, acc = 0, 0                                   # two registers: program counter, accumulator

while True:
    instr = memory[pc]          # FETCH the instruction the PC points to
    pc += 1                     # the PC moves on to the next one
    op, *arg = instr.split()    # DECODE: what to do, and with what
    if op == "LOAD":            # EXECUTE
        acc = int(arg[0])
    elif op == "ADD":
        acc += int(arg[0])
    elif op == "HALT":
        print(f"{instr:<7} -> stop")
        break
    print(f"{instr:<7} -> PC = {pc}, ACC = {acc}")
print("result in ACC:", acc)
