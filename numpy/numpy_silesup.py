import numpy as np


data1 = [ 0, 1, 2, 3, 4, 5 ]
# a1 = np.array(data1)
# print(a1)

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
# print(a2)

a3 = np.arange(12).reshape(4,3)
# print(a3)

data3 = np.array([1,2,3])
# print(data3.shape)
# print(data3.dtype)

data4 = np.array([[1,2,3], [4,5,6]])
# print(data4.shape)
# print(data4.dtype)

x1 = [1, 2, 3, 4, 5]
x2 = [6, 7, 8, 9, 10]
# data4 = np.array(x1)
# data5 = np.array([x1, x2])
# print(data4, data4.shape, data4.ndim, data4.dtype)
# print(data5, data5.shape, data5.ndim, data5.dtype)

# print(np.arange(2, 10, 2))
# print(np.zeros(4))
# print(np.zeros((3, 2)))
# print(np.eye(3))

x3 = np.array([1,2,3,4,5])
x4 = np.array([6,7,8,9,10])
# print(x3 * 2)
# print(x3 + x4)

x5 = np.array([1,2,3,4,5])
# print(x5)
# print([x5-1])
# print([x5-2])

x6 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(x6, '\n')
# print(x6[1], '\n')
# print(x6[1][1])

x7 = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15], [16,17,18,19,20]]])
# print(x7, '\n')
# print(x7[1], '\n')
# print(x7[1][1][1])
# print(x7.shape)

# print(x1[:3])
# print(x6[1][:3])
# print(x7[1][1][:3])

x8 = np.arange(28).reshape(7, 4)
# print(x8, '\n')
# x8_T = x8.T
# print(x8_T)

x9 =  np.array([2.5, 5.6, 8.1, 3.9, 5.7])
# print('합계:', np.sum(x9))
# print('평균:', np.mean(x9))
# print('표준편차:', np.std(x9, ddof=0)) # 자유도 n
# print('표준편차:', np.std(x9, ddof=1)) # 자유도 n-1
# print('분산:', np.var(x9, ddof=1))  # 자유도 n-1
# print('최솟값:', np.min(x9))
# print('최댓값:', np.max(x9))
# print('최솟값 index:', np.argmin(x9))
# print('최댓값 index:', np.argmax(x9))
# print('누적값:', np.cumsum(x9))
# print('누적곱:', np.cumprod(x9))

A = np.array([[1, 3, 5], [5, 3, 4]])
B = np.array([[1, 3], [5, 7], [5, 3]])
# print("A * B", np.dot(A, B))
# print('B의 대각원소: ', np.diag(B))
# print('B의 대각원소 합: ', np.trace(B))

A2 = np.array([[1,3,4,5], [2,5,4,8], [3,6,7,4], [6,7,2,1]])
B2 = np.array([4,3,6,7])
# print('Ax = b의 해 x: ', np.linalg.solve(A2, B2))


# print(np.random.randn())
# print(np.random.randn(5))

np.random.seed(1234) # seed 값 고정
print(np.random.randn())
print(np.random.randn(5))

np.random.seed(1234) # 동일한 seed 사용
print(np.random.randn())
print(np.random.randn(5))