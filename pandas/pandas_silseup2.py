import numpy as np
import pandas as pd
from pandas import Series

np_arr = np.array([1, 2, 3, 4])
pd_series = pd.Series([1, 2, 3, 4])

# print("np_arr: ", np_arr)
# print("np_arr shape: ", np_arr.shape)
# print("********")
# print("pd_series:\n", pd_series)
# print("pd_series shape: ", pd_series.shape)

x = Series([96, 73, 83, 97, 68, 72])
# print(x)
# print(x >= 60)

mid = Series([80, 90, 85], index=['김희영', '이원희', '박하영'])
final = Series([85, 70, 90], index=['김희영', '이원희', '박하영'])
total = mid + final
print(total)    