import matplotlib.pyplot as plt
import numpy as np

# 선 그래프
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Sine Wave", color='b')
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.title("기본 선 그래프")
plt.legend()
plt.show()
