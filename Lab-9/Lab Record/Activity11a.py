import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler
df = pd.read_csv('3Salary_Data.csv')
print('Original data:\n', df)
normalizer = Normalizer()
normalized_data = normalizer.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print('\nNormalized data:\n', normalized_df)
scaler = MinMaxScaler()
minmax_data = scaler.fit_transform(df)
minmax_df = pd.DataFrame(minmax_data, columns=df.columns)
print('\nMinMax scaled data:\n', minmax_df)
