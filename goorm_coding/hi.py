# a = '3.14'

# # print(type(a))

# # print(type(float(a)))

# b = float(a)
# print(type(b))

# if y == 3:
#     print(not y)

# N = int(input())
# i=1
# for i in range(N):
# 	i += 1
# 	sum = 1
# 	sum = sum * i 
	
# print(sum)

# N = int(input())
# S = list(map(int, input().split()))
# sorted_score = sorted(S)[-1:-4:-1]
# # for i in range(N):
# #     if S[i] in sorted_score:
# #         print(i)
# print(sorted_score)

import matplotlib.font_manager as fm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Mac 사용자는 'AppleGothic', Windows 사용자는 'Malgun Gothic')
plt.rc('font', family='AppleGothic')  
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 1. 제품 판매량 비교 (Bar Chart)
products = ["노트북", "태블릿", "스마트폰", "스마트워치", "헤드폰"]
sales = [150, 80, 300, 120, 180]

plt.figure(figsize=(8, 5))
plt.bar(products, sales, color='green')
plt.xlabel("제품명")
plt.ylabel("판매량")
plt.title("전자제품 판매량 비교")
plt.show()

# 2. 시장 점유율 분석 (Pie Chart) - 기존 데이터
companies1 = ["A사", "B사", "C사", "D사", "기타"]
market_share1 = [35, 25, 20, 10, 10]
explode1 = [0.1, 0, 0, 0, 0]  # A사 강조

plt.figure(figsize=(7, 7))
plt.pie(market_share1, labels=companies1, autopct=lambda p: f'{p:.1f}%' if p >= 10 else '', 
        explode=explode1, startangle=140)
plt.title("IT 기업 시장 점유율")
plt.show()

# 3. 시장 점유율 분석 (Pie Chart) - 10% 미만 포함 데이터
companies2 = ["A사", "B사", "C사", "D사", "E사", "F사"]
market_share2 = np.array([40, 25, 15, 8, 7, 5])  # 일부 10% 미만 포함
explode2 = [0.1, 0, 0, 0, 0, 0]  # A사 강조

plt.figure(figsize=(7, 7))
plt.pie(market_share2, labels=companies2, autopct=lambda p: f'{p:.1f}%' if p >= 10 else '', 
        explode=explode2, startangle=140)
plt.title("IT 기업 시장 점유율 (10% 미만 포함)")
plt.show() 