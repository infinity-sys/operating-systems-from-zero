# E05 exercise: -rwxr-x---  omar  ops  run.sh
import os, stat

def by_hand(rwx):                  # "rwxr-x---" -> "750"
    digits = ""
    for i in range(0, 9, 3):
        r, w, x = rwx[i:i + 3]
        n = 4 * (r == "r") + 2 * (w == "w") + 1 * (x == "x")
        digits += str(n)
    return digits

letters = "rwxr-x---"
print("digits         :", by_hand(letters))
print("group ops run? :", letters[5] == "x")
print("others read?   :", letters[6] == "r")

open("run.sh", "a").close()
os.chmod("run.sh", 0o750)                # set the bits
mode = os.stat("run.sh").st_mode         # ask the kernel
print("kernel says    :", stat.filemode(mode),
      oct(stat.S_IMODE(mode))[2:])
