import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df2=pd.read_csv(f"5ds_salaries.csv")
sns.pairplot(df2)
plt.show()
