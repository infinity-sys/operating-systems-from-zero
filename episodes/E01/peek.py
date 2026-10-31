# %%
import pandas as pd
df = pd.read_csv("../../data/processes.csv")
df.shape
# %%
df.head()
# %%
df["kind"].value_counts()
