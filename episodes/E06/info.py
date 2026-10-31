# Ask the kernel about a file: one stat call.
import os, stat, time

st = os.stat("log.txt")
print("size    :", st.st_size, "bytes")
print("mode    :", stat.filemode(st.st_mode),
      oct(stat.S_IMODE(st.st_mode))[2:])
print("inode   :", st.st_ino)
print("links   :", st.st_nlink)
print("owner   :", st.st_uid)
print("changed :", time.ctime(st.st_mtime))
