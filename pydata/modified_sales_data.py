import pandas as pd

df = pd.read_csv('/Users/goorm/Documents/GitHub/LSJ_goorm/pydata/modified_sales_data.csv')

# 1. 결측값이 포함된 행 출력하기
missing_rows = df[df.isnull().any(axis=1)]
print("결측값이 포함된 행:")
print(missing_rows)

print("\n열별 결측값 개수:")
print(df.isnull().sum())

# 2. 결측값 처리

# 숫자형 열: sales_amount는 평균으로 채우기
df['sales_amount'] = df['sales_amount'].fillna(df['sales_amount'].mean())

# discount_applied 열은 중앙값으로 채우기
df['discount_applied'] = df['discount_applied'].fillna(df['discount_applied'].median())

# 문자열 열: payment_method는 최빈값(mode)으로 채우기
if df['payment_method'].isnull().any():
    mode_payment_method = df['payment_method'].mode()[0]
    df['payment_method'] = df['payment_method'].fillna(mode_payment_method)

# 날짜 열: order_date는 날짜형으로 변환 후, 결측값은 가장 최근 날짜(max())로 채우기
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
if df['order_date'].isnull().any():
    max_date = df['order_date'].max()
    df['order_date'] = df['order_date'].fillna(max_date)

# 3. 결측값 처리 후 데이터 분석: sales_amount의 평균과 표준편차 계산
sales_mean = df['sales_amount'].mean()
sales_std = df['sales_amount'].std()

print("\nsales_amount의 평균:", sales_mean)
print("sales_amount의 표준편차:", sales_std)