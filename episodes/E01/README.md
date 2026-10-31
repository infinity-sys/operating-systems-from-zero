# E01 — What Is an Operating System?

Video: https://youtu.be/WE8zeATTRxM

Files in this folder:

- `three_jobs.py` — three Pharos jobs (backup 24 ms, web-1 3 ms, web-2 3 ms)
  scheduled two ways: arrival order vs shortest first. Prints each timeline,
  the waiting times and the average (17.0 ms vs 3.0 ms).
- `os_peek.py` — asks your operating system about itself: system name,
  machine, CPU cores, your process id and how many processes are running.
  Your numbers will differ from the video — they describe your machine.
- `peek.ipynb` (and `peek.py`, the same cells as `# %%` blocks for VS Code)
  — load `processes.csv` with pandas: shape, first rows and how many jobs of
  each kind. Run it cell by cell in Jupyter or VS Code.

The pandas scripts read `../../data/processes.csv`, so run them from inside
this folder.

```bash
python3 three_jobs.py
python3 os_peek.py
jupyter notebook peek.ipynb   # or open peek.py in VS Code
```

Requires: Python 3.10+ and pandas (`pip3 install pandas`).
