import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\python\24-11-2026\work\ai-training-week1\project\data/employees.csv")
print(df.shape)       # rows and columns
df.info()             # column types
df.describe()         # basic statistics
df.isna().sum()       # missing values
df.duplicated().sum() # repeated rows