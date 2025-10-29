T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    result = 0
    center_value = N // 2

    for i in range(N):
        if i <= center_value:
            result += sum(farm[i][center_value - i:center_value + i+1])
        if i > center_value:
            result += sum(farm[i][abs(center_value - i):N - abs(center_value - i)])
    print(f'#{t} {result}')
