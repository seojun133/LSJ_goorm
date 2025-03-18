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

# print(df)

# print('*********')
# print('행의 이름으로 검색: ',df.loc[['mid', 'final']])
# print('*********')
# print('행의 index로 검색: ',df.iloc[[0, 1]])
# print('*********')
# print('열 인덱싱:\n', df['kim'])
# print('복수 열 인덱싱:\n', df[['kim', 'lee']])

# print(df.loc[:, 'lee':'park'])
# print(df.iloc[:,:2])

# bonus = Series([3, 5, 2], index=['mid', 'report', 'final'])
# df['bon'] = bonus
# print(df)

# print(df.iloc[1]['lee']) # Series
# print(df.iloc[[1]][['lee']]) # DataFrame

df2 = df.T
# print(df2)
# print(df2[df2['mid'] > 80])
# print (df2[(df2['mid'] > 80) & (df2['final'] > 80)])


s1 = Series([1, 2, 3, 4], index=['case1', 'case2', 'case3', 'case4'])
s2 = Series([9, 8, 7, 6, 5], index= ['case5', 'case4', 'case3', 'case2', 'case1'])
# print(s1)
# print('*********')
# print(s2)

# print(s1+s2) # 한 쪽이 결측값이면 전체가 결측값이 발생 fill_value 사용 but
# print(s1.add(s2, fill_value=0)) # 서로 더하려면 add 함수를 사용

data3 = {'mid':[80, 90, 85], 'report':[10, 8,9], 'final':[85, 70, 90]}
data4 = {'mid':[70, 80, 95, 90], 'report':[9, 7, 8, 9], 'final':[95, 80, 70, 80]}

df3 = DataFrame(data3, index=['Kim', 'Lee', 'Park'])
df4 = DataFrame(data4, index=['Kim', 'Lee', 'Park', 'Choi'])

# print(df3)
# print('**********')
# print(df4)

# print(df3 + df4)
# print(df3.add(df4, fill_value=0))

