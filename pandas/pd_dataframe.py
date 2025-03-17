import pandas as pd
from pandas import DataFrame
import numpy as np
from pandas import Series

# data = {'mid':[80,90,85], 'report':[10, 8, 9], 'final':[85, 70, 90]}
# df = DataFrame(data)
# print(df)

data = np.array([[80, 90, 85], [10, 8, 9], [85, 70, 90]])
df = DataFrame(data)
# print(df)

# df = DataFrame(data, index = ['mid', 'report', 'final']) # 컬럼 추가

df = DataFrame(data, index = ['mid', 'report', 'final'], columns=['kim', 'lee', 'park'])
# print(df)

# print('행 색인:', df.index)
# print('열 색인:', df.columns)

print(df)
# print('*********')
# print('행의 이름으로 검색: ',df.loc[['mid', 'final']])
# print('*********')
# print('행의 index로 검색: ',df.iloc[[0, 1]])
# print('*********')
# print('열 인덱싱:\n', df['kim'])
# print('복수 열 인덱싱:\n', df[['kim', 'lee']])

print(df.loc[:, 'lee':'park'])
print(df.iloc[:,:2])

bonus = Series([3, 5, 2], index=['mid', 'report', 'final'])
df['bon'] = bonus
print(df)

print(df.iloc[1]['lee']) # Series
print(df.iloc[[1]][['lee']]) # DataFrame
