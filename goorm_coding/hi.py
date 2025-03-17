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

N = int(input())
S = list(map(int, input().split()))
sorted_score = sorted(S)[-1:-4:-1]
# for i in range(N):
#     if S[i] in sorted_score:
#         print(i)
print(sorted_score)