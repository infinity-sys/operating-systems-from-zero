"""Pharos Cloud: the fictional running case of "Operating Systems: From Zero to Hero".
Pharos Cloud is a FICTIONAL small hosting company in Alexandria, Egypt, that runs one busy
Linux server, pharos-01. Every number here is synthetic. Generated ONCE with a fixed seed.
Run:  python3 make_pharos.py   (writes the CSVs next to this file)
"""
import csv, random, os
SEED = 1969            # the year Unix was born
rng = random.Random(SEED)
HERE = os.path.dirname(os.path.abspath(__file__))
def w(name, header, rows):
    with open(os.path.join(HERE, name), "w", newline="") as f:
        c = csv.writer(f); c.writerow(header); c.writerows(rows)

# 1. processes.csv: the jobs that reach pharos-01's CPU on one busy morning
kinds = {  # kind: (names, users, burst range ms, priority range, memory MB range, io_bound prob)
    "web":    (["nginx-worker", "php-fpm", "api-gateway"], ["www"], (2, 8), (1, 2), (40, 160), 0.8),
    "db":     (["postgres", "redis"], ["postgres", "redis"], (4, 14), (1, 3), (200, 900), 0.6),
    "batch":  (["invoice-report", "payroll-export", "csv-import"], ["salma", "omar", "karim"], (10, 30), (3, 4), (120, 600), 0.2),
    "backup": (["backup.sh", "rsync-offsite"], ["root"], (18, 40), (4, 5), (60, 200), 0.7),
    "ml":     (["train_model.py", "forecast.py"], ["nour", "youssef"], (20, 45), (3, 5), (800, 2400), 0.1),
    "system": (["cron", "sshd", "logrotate", "systemd-journal"], ["root"], (1, 4), (1, 2), (8, 40), 0.5),
}
weights = {"web": 14, "db": 8, "batch": 8, "backup": 4, "ml": 4, "system": 10}
pool = [k for k, n in weights.items() for _ in range(n)]
rng.shuffle(pool)
rows, t = [], 0
for i, k in enumerate(pool):
    names, users, (b0, b1), (p0, p1), (m0, m1), io = kinds[k]
    t += rng.choice([0, 1, 1, 2, 2, 3, 4, 5])
    rows.append([1000 + 7 * i + rng.randint(0, 6), rng.choice(names), rng.choice(users), k, t,
                 rng.randint(b0, b1), rng.randint(p0, p1), rng.randint(m0, m1) // 4 * 4,
                 "yes" if rng.random() < io else "no"])
w("processes.csv", ["pid", "name", "user", "kind", "arrival_ms", "burst_ms", "priority", "memory_mb", "io_bound"], rows)

# 2. page_refs.csv: three page-reference strings (pages 0-7), 20 references each
refs = []
for s in ("A", "B", "C"):
    hot = rng.sample(range(8), 4)
    for j in range(20):
        p = rng.choice(hot) if rng.random() < 0.75 else rng.randrange(8)
        refs.append([s, j + 1, p])
w("page_refs.csv", ["string", "seq", "page"], refs)

# 3. disk_requests.csv: one queue of 10 cylinder requests on a 200-cylinder disk (0-199)
head = rng.randint(40, 70)
cyl = rng.sample(range(200), 10)
w("disk_requests.csv", ["order", "cylinder", "head_start"], [[j + 1, c, head] for j, c in enumerate(cyl)])

# 4. banker.csv: 5 processes x 3 resource types (A, B, C) for deadlock avoidance; must be a SAFE state
def safe(alloc, mx, avail):
    need = [[m - a for m, a in zip(mr, ar)] for mr, ar in zip(mx, alloc)]
    work, done, order = list(avail), [False] * len(alloc), []
    while len(order) < len(alloc):
        for i in range(len(alloc)):
            if not done[i] and all(n <= x for n, x in zip(need[i], work)):
                work = [x + a for x, a in zip(work, alloc[i])]; done[i] = True; order.append(i); break
        else:
            return None
    return order
while True:
    total = [rng.randint(8, 12), rng.randint(4, 7), rng.randint(6, 9)]
    alloc = [[rng.randint(0, 3) for _ in range(3)] for _ in range(5)]
    used = [sum(a[j] for a in alloc) for j in range(3)]
    if any(u >= tt for u, tt in zip(used, total)):
        continue
    avail = [tt - u for tt, u in zip(total, used)]
    mx = [[a + rng.randint(0, 4) for a in ar] for ar in alloc]
    if any(m > tt for mr in mx for m, tt in zip(mr, total)):
        continue
    o = safe(alloc, mx, avail)
    if o and o != list(range(5)):
        break
w("banker.csv", ["process", "alloc_A", "alloc_B", "alloc_C", "max_A", "max_B", "max_C"],
  [[f"P{i}", *alloc[i], *mx[i]] for i in range(5)])
w("resources.csv", ["resource", "total", "available"], [[r, total[j], avail[j]] for j, r in enumerate("ABC")])
print("processes", len(rows), "| refs", len(refs), "| disk head", head, "| banker safe order", ["P%d" % i for i in o])
