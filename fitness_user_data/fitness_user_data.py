import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/goorm/Documents/GitHub/LSJ_goorm/fitness_user_data/fitness_user_data.csv')

print("기본 정보 확인")
df.info()
print("\n처음 5행 출력")
print(df.head())
print("\n결측값 현황")
print(df.isnull().sum())

# 데이터 전처리

# (1) 결측값 처리
df['exercise_time'].fillna(df['exercise_time'].mean(), inplace=True)
df['calories_burned'].fillna(0, inplace=True)
df['weight'].fillna(df['weight'].mode()[0], inplace=True)

# (2) 이상치 처리
exercise_time_90 = df['exercise_time'].quantile(0.9)
df.loc[df['exercise_time'] >= 180, 'exercise_time'] = exercise_time_90

calories_burned_75 = df['calories_burned'].quantile(0.75)
df.loc[df['calories_burned'] >= 1500, 'calories_burned'] = calories_burned_75

# (3) 날짜 처리
df['exercise_date'] = pd.to_datetime(df['exercise_date'], errors='coerce')
df['exercise_day_of_week'] = df['exercise_date'].dt.day_name()

# 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 시각화

# (1) 운동시간 / 소모 칼로리
plt.figure(figsize=(8, 6))
plt.plot(df['exercise_time'], df['calories_burned'], 'o', alpha=0.7)
plt.title('운동 시간과 소모 칼로리 관계', fontsize=16)
plt.xlabel('운동 시간(분)', fontsize=12)
plt.ylabel('소모 칼로리', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# (2) 운동유형 / 소모 칼로리
plt.figure(figsize=(10, 6))
exercise_types = df['exercise_type'].unique()
x_values = [np.where(exercise_types == x)[0][0] for x in df['exercise_type']]

plt.plot(x_values, df['calories_burned'], 'o', alpha=0.7)
plt.xticks(range(len(exercise_types)), exercise_types)
plt.title('운동 유형과 소모 칼로리 관계', fontsize=16)
plt.xlabel('운동 유형', fontsize=12)
plt.ylabel('소모 칼로리', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# (3) 운동시간 / 몸무게
plt.figure(figsize=(8, 6))
plt.plot(df['exercise_time'], df['weight'], 'o', alpha=0.7)
plt.title('운동 시간과 몸무게 관계', fontsize=16)
plt.xlabel('운동 시간(분)', fontsize=12)
plt.ylabel('몸무게 (kg)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

