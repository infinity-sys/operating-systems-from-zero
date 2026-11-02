# E10 exercise: P and Q each run "x = x + 1" twice (read x, then write x + 1); x starts at 0.
# Try EVERY interleaving of the 8 steps and collect the final values.
from itertools import combinations
from collections import Counter
finals = Counter()
for p_slots in combinations(range(8), 4):          # which of the 8 steps belong to P
    x, local, step = 0, {"P": 0, "Q": 0}, {"P": 0, "Q": 0}
    for k in range(8):
        who = "P" if k in p_slots else "Q"
        if step[who] % 2 == 0: local[who] = x      # read
        else: x = local[who] + 1                   # write
        step[who] += 1
    finals[x] += 1
print("interleavings :", sum(finals.values()))
for v in sorted(finals): print(f"final x = {v}   : {finals[v]:>2} interleavings")
print("max, min      :", max(finals), min(finals))
