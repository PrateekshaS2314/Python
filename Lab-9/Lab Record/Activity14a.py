import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"5ds_salaries.csv")
df.columns
df.skew(numeric_only=True)
df.kurt(numeric_only=True)
sns.histplot(df["salary_in_usd"])
plt.show()
sns.histplot(df["salary_in_usd"],kde=True)
plt.show()
sns.distplot(df["salary_in_usd"])
