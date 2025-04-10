import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
df = pd.read_csv('4laptops.csv')
le = LabelEncoder()
df['Storage'] = le.fit_transform(df['Storage'])
column_name = 'Operating System' 
ohe = OneHotEncoder(sparse=False, drop='first')
os_encoded = ohe.fit_transform(df[[column_name]])
os_encoded_df = pd.DataFrame(os_encoded, columns=ohe.get_feature_names_out([column_name]))
final = pd.concat([df, os_encoded_df], axis=1)
print("Original + Encoded Data:\n")
print(final)
