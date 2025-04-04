# import matplotlib.pyplot as plt
# import numpy as np

# # x 범위 설정
# x = np.linspace(-2, 8, 100)

# # 함수 정의
# y1 = 2*x + 3  # 선형 함수
# y2 = x**2 - 6*x + 8  # 2차 함수

# # 그래프 그리기
# plt.figure(figsize=(10, 6))
# plt.plot(x, y1, label='f(x)=2x+3')
# plt.plot(x, y2, label='f(x)=x²-6x+8')

# # x축, y축 그리기
# plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
# plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# # 꼭짓점 구하기 (2차 함수만)
# vertex_x = 6/2  # -b/2a where a=1, b=-6
# vertex_y = (vertex_x**2) - 6*vertex_x + 8
# plt.plot(vertex_x, vertex_y, 'ro', label=f'꼭짓점 ({vertex_x}, {vertex_y})')

# # x절편 구하기
# # 선형 함수: 2x + 3 = 0 -> x = -3/2
# x1_linear = -3/2
# plt.plot(x1_linear, 0, 'go', label=f'선형함수 x절편 ({x1_linear}, 0)')

# # 2차 함수: x² - 6x + 8 = 0 -> (x-2)(x-4) = 0 -> x = 2 or x = 4
# x1_quad = 2
# x2_quad = 4
# plt.plot([x1_quad, x2_quad], [0, 0], 'bo', label='2차함수 x절편')

# # y절편 구하기
# plt.plot(0, 3, 'mo', label='선형함수 y절편 (0, 3)')
# plt.plot(0, 8, 'ko', label='2차함수 y절편 (0, 8)')

# plt.grid(True)
# plt.legend()
# plt.title('함수 그래프')
# plt.xlabel('x')
# plt.ylabel('y')

# # 결과 출력
# print("1. 꼭짓점 좌표:")
# print(f"   2차 함수: ({vertex_x}, {vertex_y})")
# print("\n2. x절편:")
# print(f"   선형 함수: ({x1_linear}, 0)")
# print(f"   2차 함수: ({x1_quad}, 0), ({x2_quad}, 0)")
# print("\n3. y절편:")
# print("   선형 함수: (0, 3)")
# print("   2차 함수: (0, 8)")

# plt.show()

    import matplotlib.pyplot as plt
    import numpy as np

    # f(x)=2x+3 (선형 함수)
    x_linear = np.linspace(-5, 5, 100)
    y_linear = 2 * x_linear + 3
    # x절편: 2x+3=0 → x=-3/2, y=0, y절편: f(0)=3 → (0,3)
    plt.plot(x_linear, y_linear, label='f(x)=2x+3')
    plt.scatter([-3/2, 0], [0, 3], color='red')  # x절편과 y절편 표시
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)=2x+3')
    plt.legend()
    plt.grid(True)
    plt.show()

    # f(x)=x^2-6x+8 (2차 함수)
    x_quad = np.linspace(-2, 8, 100)
    y_quad = x_quad**2 - 6*x_quad + 8
    # 꼭짓점: x=-b/(2a)=3, y=f(3)=9-18+8=-1 → (3, -1)
    # x절편: (x-2)(x-4)=0 → x=2,4 → (2,0)와 (4,0)
    # y절편: f(0)=8 → (0,8)
    plt.plot(x_quad, y_quad, label='f(x)=x^2-6x+8')
    plt.scatter([3, 2, 4, 0], [-1, 0, 0, 8], color='red')  # 꼭짓점, x절편, y절편 표시
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)=x^2-6x+8')
    plt.legend()
    plt.grid(True)
    plt.show()