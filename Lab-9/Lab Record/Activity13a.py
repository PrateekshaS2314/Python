# groupby
import pandas as pd

# Sample sales data
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Grocery'],
    'Sales': [1200, 1500, 800, 900, 400]
}
df = pd.DataFrame(data)

# Group by Category and calculate median sales
median_sales = df.groupby('Category')['Sales'].median().reset_index()

print("Grouped by Category (Median Sales):\n", median_sales)
# merge
# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df2 = pd.DataFrame({
    'ID': [3, 4],
    'City': ['Paris', 'London']
})
# Outer join on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='outer')
print("\nMerged (Outer Join):\n", merged_df)
# concat
# Two DataFrames to concatenate side-by-side (horizontally)
df_a = pd.DataFrame({'A': [1, 2, 3]})
df_b = pd.DataFrame({'B': ['X', 'Y', 'Z']})

# Concatenate along columns (axis=1)
concat_df = pd.concat([df_a, df_b], axis=1)
print("\nConcatenated DataFrame (Horizontally):\n", concat_df)
