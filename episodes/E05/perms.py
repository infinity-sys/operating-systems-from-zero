# Read the permission bits of every file, two ways.
import os, stat

def by_hand(rwx):                  # "rw-r--r--" -> "644"
    digits = ""
    for i in range(0, 9, 3):
        r, w, x = rwx[i:i + 3]
        n = 4 * (r == "r") + 2 * (w == "w") + 1 * (x == "x")
        digits += str(n)
    return digits

for name in sorted(os.listdir(".")):
    mode = os.stat(name).st_mode
    text = stat.filemode(mode)                 # like ls -l
    real = oct(stat.S_IMODE(mode))[2:]         # from kernel
    print(f"{name:10} {text}  hand {by_hand(text[1:])}"
          f"  kernel {real}")
