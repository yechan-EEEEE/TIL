T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(8):
        if N >= money[i]:
            result[i] = N // money[i]
            N %= money[i]
    print(f'#{tc}')
    print(*result)