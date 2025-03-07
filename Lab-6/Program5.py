# Create a DataFrame from a dictionary
import pandas as pd
data = {
"Name": ["Ram", "Robert", "Rahim"],
"Age": [25, 30, 35],
"City": ["Ayodya", "Chennai", "Delhi"],
}
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.index, type(df.index))
