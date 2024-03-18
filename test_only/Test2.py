import pandas as pd

data = [[1, 2, 3], [1, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data, columns=["a", "b", "c"])

print(df.groupby(by=["a"]).groups.keys())
