import pandas as pd

to_path = r"C:\Users\data\Sampledata.csv"
df = pd.read_excel(r"C:\Users\data\Sampledata.xlsx", index_col=[1, 2], header=[2], sheet_name=None)
print(df)
df = pd.DataFrame.from_dict(df)
df.to_csv(to_path)


