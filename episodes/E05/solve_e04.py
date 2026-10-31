# E04 exercise: an app prints a file on a microkernel.
# Every message goes through the kernel.
trip = ["app", "print", "file",   # the servers
        "driver"]
back = trip[::-1]                  # replies return
path = trip + back[1:]             # app ... driver ... app

messages = len(path) - 1
entries = messages                 # one per message
switches = 2 * entries             # in and out each time

print("path    :", " -> ".join(path))
print("messages:", messages)
print("kernel entries:", entries)
print("mode switches :", switches)
