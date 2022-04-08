import pandas as pd

df = pd.read_csv('data.csv')
print(df)

df.loc[-1]=[124,1253]
df.to_csv('data.csv')
