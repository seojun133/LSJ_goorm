import matplotlib.pyplot as plt
import numpy as np

# 30일간의 온도, 습도, 토양 수분 데이터 생성 (NumPy 사용)
temperature = np.random.randint(15, 35, (30,))
humidity = np.random.randint(10, 50, (30,))
soil_moisture = np.random.randint(5, 40, (30,))

# 모든 센서 값이 25 이상인 날짜 찾기
valid_days_numpy = np.where((temperature >= 25) & (humidity >= 25) & (soil_moisture >= 25))[0] + 1

# 최종 결과 출력
{
    "Temperature": temperature.tolist(),
    "Humidity": humidity.tolist(),
    "Soil Moisture": soil_moisture.tolist(),
    "Valid Days (All ≥ 25)": valid_days_numpy.tolist()
}
# 30일 동안의 날짜 생성
days = np.arange(1, 31)

# 그래프 크기 설정
plt.figure(figsize=(12, 6))

# 온도, 습도, 토양 수분 데이터 플로팅
plt.plot(days, temperature, marker='o', linestyle='-', label='Temperature', color='red')
plt.plot(days, humidity, marker='s', linestyle='-', label='Humidity', color='blue')
plt.plot(days, soil_moisture, marker='^', linestyle='-', label='Soil Moisture', color='green')

# 모든 값이 25 이상인 날짜에 마커 추가
plt.scatter(valid_days_numpy, temperature[valid_days_numpy - 1], color='black', label='Valid Days', zorder=3)

# 그래프 제목 및 라벨 추가
plt.title('Smart Farm Sensor Data Over 30 Days')
plt.xlabel('Day')
plt.ylabel('Sensor Readings')
plt.xticks(days)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# 그래프 표시
plt.show()


