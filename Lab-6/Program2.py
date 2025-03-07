import pandas as pd
import numpy as np
# Create a Series from a list
data = [1, 3, 5, np.nan, 6]
s2 = pd.Series((data), index=['a', 'b', 'c', 'd','e'])
print(s2)
