# E03 exercise: open, read, print, exit.
# Mark every user -> kernel -> user switch.
calls = ["open", "read", "write", "close", "exit"]

switches = 0
for n, name in enumerate(calls, 1):
    switches += 1                # into the kernel
    if name == "exit":
        print(f"{n}. {name:5}: user -> kernel"
              " (never returns)")
    else:
        switches += 1            # back to user mode
        print(f"{n}. {name:5}: user -> kernel -> user")

print("system calls :", len(calls))
print("mode switches:", switches)
