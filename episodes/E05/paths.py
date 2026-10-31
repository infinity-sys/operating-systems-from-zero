# Follow a list of cd commands, like the shell does.
import posixpath as pp

home = "/home/box"
where = home
for target in ["pharos", "../..", "/etc", "~"]:
    if target == "~":
        new = home                       # ~ means home
    else:
        new = pp.join(where, target)     # absolute wins
    where = pp.normpath(new)             # fold . and ..
    print(f"cd {target:7} -> {where}")
