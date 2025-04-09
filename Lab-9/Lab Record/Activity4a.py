import pandas as pd

# Read the CSV file
df = pd.read_csv("1experience.csv")

# 1. Display the first 3 rows
print("last 3 rows:")
print(df.tail(3))
print("\n")

# 2. Display the description (summary statistics)
print("Description of df:")
print(df.describe(),"\n")

# 3. Display DataFrame information
print("Information of df:")
print(df.info())
print("\n")

# 5. Display the 1st column using iloc
print("column name:")
print(df.columns.tolist())
