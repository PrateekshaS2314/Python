# Create a DataFrame from a date_range()
import pandas as pd
import numpy as np
dates = pd.date_range("20130101", periods=6)
df_2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(dates)
print(df_2)
