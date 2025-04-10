import pandas as pd
products = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 60000},
    {'name': 'Chair', 'category': 'Furniture', 'price': 3000},
    {'name': 'Pen', 'category': 'Stationery', 'price': 50}
]
df = pd.DataFrame(products)
df['discounted_price'] = df['price'] * 0.90
print("Product DataFrame with discounted price:")
print(df)
