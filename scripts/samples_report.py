import pandas as pd
df = pd.read_csv("data/samples.csv")
print(df["organism"].value_counts())
print(df.groupby("organism")["gc_content"].mean())
print(df.groupby("organism")["length"].mean())
long_samples = df[df["length"]>1000]
long_samples.to_csv("results/long_samples.csv", index=False)
rows = [{"name": "seq1", "gc": 41.2}, {"name": "seq2", "gc": 52.0}]
pd.DataFrame(rows)
print(pd.DataFrame(rows))