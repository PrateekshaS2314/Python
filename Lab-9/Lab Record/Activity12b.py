import pandas as pd
df=pd.read_csv('4laptops.csv')
df
q1 = df['Screen'].quantile(0.25)
q3 = df['Screen'].quantile(0.75)

iqr=q3-q1
lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr
outliers=df[(df['Screen']<lower_bound) | (df['Screen']>upper_bound)]
print("q1:",q1)
print("q3:",q3)
print("iqr:",iqr)
print("lower_bound:",lower_bound)
print("upper_bound:",upper_bound)
print("outliers:",outliers)
