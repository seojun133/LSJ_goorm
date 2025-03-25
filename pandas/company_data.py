import numpy as np
import matplotlib.pyplot as plt


plt.rc('font', family='AppleGothic')  
plt.rcParams['axes.unicode_minus'] = False

# 1. 제품 판매량 비교 (Bar Chart)
products = ["노트북", "태블릿", "스마트폰", "스마트워치", "헤드폰"]
sales = [150, 80, 300, 120, 180]

plt.figure(figsize=(8, 5))
plt.bar(products, sales, color='green')
plt.xlabel("제품명")
plt.ylabel("판매량")
plt.title("전자제품 판매량 비교")
plt.show()

# 2. 시장 점유율 분석 (Pie Chart) - 10% 이상만 퍼센트 표시
companies = ["A사", "B사", "C사", "D사", "E사", "F사"]
market_share = np.array([40, 25, 15, 8, 7, 5])
explode = [0.1, 0, 0, 0, 0, 0]

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    market_share, labels=companies, explode=explode, startangle=140, autopct="%1.1f%%"
)
# 10% 미만 퍼센트 숨기기
for i, pct in enumerate(market_share):
    if pct < 10:
        autotexts[i].set_text("")


plt.title("IT 기업 시장 점유율")
plt.show()