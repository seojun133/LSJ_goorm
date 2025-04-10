print('+와 -를 번갈아가며 출력하세요.')
n = int(input('몇 개를 출력할까요?'))

for _ in range(n // 2):
    print('+ -', end =' ')

if n % 2:
    print('+', end='')

print()