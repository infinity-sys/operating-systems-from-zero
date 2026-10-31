# Count mode switches for one request:
# "read a block from a file", in three designs.
# Each step: (who runs, in which mode).
designs = {
    "monolithic": [
        ("app", "user"), ("kernel", "kernel"),
        ("app", "user")],
    "layered (4 layers)": [
        ("app", "user"), ("kernel", "kernel"),
        ("app", "user")],
    "microkernel": [
        ("app", "user"), ("kernel", "kernel"),
        ("file server", "user"), ("kernel", "kernel"),
        ("disk driver", "user"), ("kernel", "kernel"),
        ("file server", "user"), ("kernel", "kernel"),
        ("app", "user")],
}

for name, path in designs.items():
    modes = [mode for who, mode in path]
    sw = sum(a != b for a, b in zip(modes, modes[1:]))
    msgs = sum(w == "kernel" for w, m in path)
    print(f"{name:19}: switches {sw}, "
          f"kernel entries {msgs}")
