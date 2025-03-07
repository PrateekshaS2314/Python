import pandas as pd
import numpy as np
A = np.random.randn(5, 3)
print(A, type(A),"\n")
dfA = pd.DataFrame(A)
print(dfA,type(dfA))
