import pandas as pd
# Create a DataFrame from a dictionary
data = {'Name': ['Ram', 'Robert','Rahim'],
'Age': [25, 30, 35],
'City': ['Ayodya', 'Chennai', 'Delhi']}
df = pd.DataFrame(data)
print(df)
print("---------")
filtered_df = df[df["Age"] > 25]
print(filtered_df)
