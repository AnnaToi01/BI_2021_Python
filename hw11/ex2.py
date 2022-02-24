import pandas as pd
from io import StringIO
import requests

r = requests.get("https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv")
data = StringIO(r.text)
df = pd.read_csv(data, sep=",")
df_part = df[df["matches"] > df["matches"].mean()][["pos", "reads_all", "mismatches", "deletions", "insertions"]]
df_part.to_csv("train_part.csv")
